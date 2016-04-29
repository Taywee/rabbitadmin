# rabbitadmin
Another simple python module for managing rabbitmq connections.  Written for python 3.4, though 2.7 should work as well.

This is done in multiple steps (manageable by a makefile).

First, the api.json file needs to be manually built out.  This is necessary, in
order to properly format it, as the documentation isn't consistent.

Then, makejsonapiclient.py is used to build the python Code (in a Rabbit class).

One of the possible init parameters for the class is http, which is a class
that should be inited with a username, password, hostname, scheme, and port
number.  It should have a __call__ method which can accept a single
convertable-to-json payload, and should return either the deserialized json
response or None. The class is built and used internally.  A standard
rabbitadmin.http class is included, and is used by default.
