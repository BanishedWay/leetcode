#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'字符画及其原理'

__author__ = 'BanishedWay'

# 先准备一个字符集
char_set = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. """

# 将图片转化成灰度图
from PIL import Image
import os

print(os.getcwd())

im = Image.open('./autumn.jpg')
im = im.resize((160, 90), Image.ANTIALIAS)
im = im.convert('L')  # 黑白图
im.save('test.jpg')


# 接下来将灰度值转成字符
def get_char(gray):
    if gray >= 240:
        return ' '
    else:
        return char_set[int(gray / ((256.0 + 1) / len(char_set)))]


text = ''
for i in range(im.height):
    for j in range(im.width):
        gray = im.getpixel((j, i))
        if isinstance(gray, tuple):
            gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 0.0722 * gray[2])
        text += get_char(gray)
    text += '\n'

with open('pic.txt', 'w') as f:
    f.write(text)
