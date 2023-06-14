#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'下载文件并添加进度条'

__author__ = 'BanishedWay'

# 使用requests进行下载
import requests
from clint.textui import progress

url = 'https://th.wallhaven.cc/small/l8/l83o92.jpg'
res = requests.get(url)

with open('./Exercise/day04/test.png', 'wb') as f:
    f.write(res.content)

# 下载大文件的话设置stream=True，只有当我们遍历iter_content时才会下载
# 同时可以添加进度条显示下载进度

url = 'https://download.jetbrains.com.cn/idea/ideaIC-2023.1.2.exe'
res = requests.get(url, stream=True)

total_length = int(res.headers.get('content-length'))

with open('idea.exe', 'wb') as idea:
    # for chunk in res.iter_content(chunk_size=1024):
    #     if chunk:
    #         idea.write(chunk)
    for chunk in progress.bar(res.iter_content(chunk_size=1024),
                              expected_size=(total_length / 1024) + 1,
                              width=100):
        if chunk:
            idea.write(chunk)