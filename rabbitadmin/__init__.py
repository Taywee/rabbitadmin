#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2016 Taylor C. Richberger <taywee@gmx.com>
# This code is released under the license described in the LICENSE file

from .rabbit import Rabbit

try:
    # python 2.x
    from urllib import quote as urlquote
except ImportError:
    # python 3.x
    from urllib.parse import quote as urlquote
