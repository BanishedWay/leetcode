#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'找到大文件'

__author__ = 'BanishedWay'

import os


def get_big_file(path, filesize):
    # 遍历指定目录下大小大于filesize的文件
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            # 是否是文件
            if not os.path.isfile(target_file):
                continue
            size = os.path.getsize(target_file)
            if size > filesize:
                # 输出目标大文件的信息
                size = size // (1024 * 1024)  # 转换为M
                size = '{_size}M'.format(_size=size)
                print(target_file, size)


if __name__ == '__main__':
    get_big_file('/home/ubuntu/documents/leetcode', 500 * 1024)
