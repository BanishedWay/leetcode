#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'UDP编程服务器'

__author__ = 'BanishedWay'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
# 不需要listen
while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Recieved from %s:%s.' % addr)
    s.sendto(b'Hello %s!' % data, addr)
