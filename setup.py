#!/usr/bin/env python3

from setuptools import setup

version = '1.0.6'

setup(name='rabbitadmin',
    version=version,
    description="A simple rabbitmq management module, autogenerated from the documentation",

    long_description="""\
If you are running RabbitMQ, you can find your documentation at http://localhost:15672/api/.
Otherwise, the docs are at
https://cdn.rawgit.com/rabbitmq/rabbitmq-management/rabbitmq_v3_6_1/priv/www/api/index.html""",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='python http amqp rabbit rabbitmq management',
    author='Taylor C. Richberger <tcr@absolute-performance.com>',
    author_email='tcr@absolute-performance.com',
    url='https://github.com/Taywee/rabbitadmin',
    download_url='https://github.com/Taywee/rabbitadmin',
    license='MIT',
    packages=['rabbitadmin'],
    include_package_data=False,
    zip_safe=False,
    )
