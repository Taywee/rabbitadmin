#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

import argparse
import json
import sys

def make_json_api_client(
    api: list,
    outfile = sys.stdout,
    classname: str = "Client",
    imports: list = None,
    defaultclass: str = None,
    indent: str = '    ',
    ):

    if imports:
        outfile.writelines('{}\n'.format(imp.strip()) for imp in imports)
    outfile.write('\n')
    outfile.write('''class {name}(object):
{i}def __init__(self, scheme, host, port, username, password, httpclass{defaultclass}):
{i}{i}self.connection = httpclass(
{i}{i}{i}scheme=scheme,
{i}{i}{i}host=host,
{i}{i}{i}port=port,
{i}{i}{i}username=username,
{i}{i}{i}password=password,
{i}{i}{i})
'''.format(
            name=classname,
            defaultclass=(' = {}'.format(defaultclass) if defaultclass else ''),
            i=indent,
            )
        )
    outfile.write('\n')

def main():
    parser = argparse.ArgumentParser(description="Generate a python API class to interface with some json API")
    parser.add_argument('-i', '--input', help="Input JSON API file, defaults to stdin")
    parser.add_argument('-o', '--output', help="Output python file path, defaults to stdout")
    parser.add_argument('-c', '--classname', help="API class name, defaults to %(default)s", default="Client")
    parser.add_argument('-I', '--imports', help="Import statements.  May be specified multiple times", action='append', default=[])
    parser.add_argument('--indent', help="Indenting string.  Defaults to '\\t'", default='\t')
    parser.add_argument('-d', '--default-http-class', help="Default http class.  Without this, you will be required to specify your own")
    args = parser.parse_args()

    if args.input is None:
        input = sys.stdin
    else:
        input = open(args.input, 'r')

    if args.output is None:
        output = sys.stdout
    else:
        output = open(args.output, 'r')

    with input as i, output as o:
        make_json_api_client(
            api=json.load(input),
            outfile=o,
            classname=args.classname,
            imports=args.imports,
            defaultclass=args.default_http_class,
            indent=args.indent,
            )

if __name__ == '__main__':
    main()
