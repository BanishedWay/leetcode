#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'UDP客户端'

__author__ = 'BanishedWay'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Mike', b'Jack', b'Tom']:
    s.sendto(data, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
