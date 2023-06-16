#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"token生成"

__author__ = "BanishedWay"

# 生成token
import time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

SECRET_KEY = 'owiernwertwet'
s = Serializer(SECRET_KEY, 3)
data = s.dump({'user_id': 343})
token = data.decode()
print(token)

# 解析token
time.sleep(2)
serializer = Serializer(SECRET_KEY)
data = serializer.loads(token)
print(data)
