#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'测试WSGI服务'

__author__ = 'BanishedWay'


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']