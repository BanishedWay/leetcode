#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'WSGI server'

__author__ = 'BanishedWay'

from wsgiref.simple_server import make_server
from hello import application

# 创建服务器
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听
httpd.serve_forever()