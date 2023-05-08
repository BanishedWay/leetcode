#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"测试itertools"

__author__ = 'BanishedWay'

import itertools

for c in itertools.chain('ABC', 'XYZ'):
    print(c, end=" ")
