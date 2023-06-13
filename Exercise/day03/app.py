#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'制作密码生成器'

__author__ = 'BanishedWay'
"""
密码生成规则
1. 密码长度不能小于8
2. 密码可以包括英文字母、数字、符号
3. 至少包含一个大写字母
4. 至少包含一个特殊符号
"""

import random


# 生成大写字母
def get_upper():
    # 随机生成至少一个大写字母
    count = random.randint(1, 3)
    return random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=count)


# 生成特殊字符
def get_special():
    # 随机生成至少一个特殊字符
    count = random.randint(1, 3)
    return random.choices('!@#$%^&*()_+~', k=count)


# 生成特定数目的小写字母和数字
def get_lower(count):
    string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return random.choices(string, k=count)


# 生成特定长度的密码
def get_password(length):
    if length < 8:
        length = 8
    password = []

    upper_list = get_upper()
    special_list = get_special()
    password.extend(upper_list)
    password.extend(special_list)

    surplus_length = length - len(password)
    lower_list = get_lower(surplus_length)
    password.extend(lower_list)

    # 打乱顺序
    random.shuffle(password)
    return ''.join(password)


if __name__ == '__main__':
    print(get_password(8))
    print(get_password(16))
    print(get_password(4))