#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'测试WSGI服务'

__author__ = 'BanishedWay'


# 读取PATH_INFO
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # return [b'<h1>Hello, web!</h1>']
    # 在environ中读取PATH_INFO
    body = '<h1>Hello, %s!<h1>' % (
        environ['PATH_INFO'].encode('iso-8859-1').decode('utf8')[1:] or 'web')
    return [body.encode('utf-8')]