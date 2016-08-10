#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2016 Absolute Performance Inc <csteam@absolute-performance.com>.
# All rights reserved.
# This is proprietary software.
# No warranty, explicit or implicit, provided.

import unittest
import tempfile
from rabbitadmin import Client as Rabbit
import six
from requests import HTTPError

class RabbitTest(unittest.TestCase):
    def setUp(self):
        self.credentials = {'username': 'guest', 'password': 'guest'}

        self.rabbit = Rabbit(scheme='http', host='localhost', port=15672, **self.credentials)

        self.vhost = 'rabbitadmin_test_vhost'

        self.rabbit.put_vhost(vhost=self.vhost)
        self.rabbit.put_user_vhost_permissions(vhost=self.vhost, user=self.credentials['username'], configure='^.*$', write='^.*$', read='^.*$')

    def tearDown(self):
        self.rabbit.delete_vhost(vhost=self.vhost)
    
    def test_user(self):
        with self.rabbit as rabbit:
            user = {'username': 'testuser', 'password': 'testpass'}
            # User does not yet exist
            with six.assertRaisesRegex(self, HTTPError, 'Unauthorized'):
                Rabbit(scheme='http', host='localhost', port=15672, **user).get_aliveness_test(vhost=self.vhost)

            rabbit.put_user(user=user['username'], password=user['password'], tags='monitoring')

            # User doesn't have permissions on the vhost
            with six.assertRaisesRegex(self, HTTPError, 'Unauthorized'):
                Rabbit(scheme='http', host='localhost', port=15672, **user).get_aliveness_test(vhost=self.vhost)

            # User needs permissions to create and destroy the test queue
            rabbit.put_user_vhost_permissions(vhost=self.vhost, user=user['username'], configure='^.*$', write='^.*$', read='^.*$')

            # User needs the right password
            with six.assertRaisesRegex(self, HTTPError, 'Unauthorized'):
                Rabbit(scheme='http', host='localhost', port=15672, username=user['username'], password='wrongpassword').get_aliveness_test(vhost=self.vhost)

            # This should work
            Rabbit(scheme='http', host='localhost', port=15672, **user).get_aliveness_test(vhost=self.vhost)
            rabbit.delete_user(user['username'])

    def test_queue(self):
        with self.rabbit as rabbit:
            queue = 'rabbitadmin_test_queue_queue'
            exchange = 'rabbitadmin_test_queue_exchange'
            testmessage = 'This is a test message'
            rabbit.put_queue(vhost=self.vhost, queue=queue)
            rabbit.put_exchange(vhost=self.vhost, exchange=exchange)
            rabbit.post_binding_by_queue(vhost=self.vhost, exchange=exchange, queue=queue)

            rabbit.post_exchange(vhost=self.vhost, exchange=exchange, payload=testmessage, properties={}, routing_key="", payload_encoding="string")
            self.assertEqual(rabbit.post_queue_get(vhost=self.vhost, queue=queue, count=1, requeue=False, encoding="auto", truncate='50000')[0]['payload'], testmessage)

            for binding in rabbit.get_bindings_by_queue(vhost=self.vhost, exchange=exchange, queue=queue):
                rabbit.delete_binding_by_queue(vhost=binding['vhost'], exchange=binding['source'], queue=binding['destination'], props=binding['properties_key'])
            rabbit.delete_exchange(vhost=self.vhost, exchange=exchange)
            rabbit.delete_queue(vhost=self.vhost, queue=queue)



if __name__ == '__main__':
    unittest.main()
