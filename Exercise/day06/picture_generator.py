#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"生成图片验证码"

__author__ = "BanishedWay"

import base64
import os
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont


# 生成随机颜色
def random_color():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return c1, c2, c3


# 生成一张指定大小的图片
def generate_picture(width=120, height=35):
    image = Image.new('RGB', (width, height), random_color())
    return image


# 生成随机数字和字母
def random_str():
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_char = random.choice([random_num, random_low_alpha])
    return random_char


# 在image上添加数字和字母
def draw_str(count: int, image, font_size: int):
    """
    在图片上写随机字符
    :param count: 字符数量
    :param image: 图片数量
    :param font_size: 字体大小
    :return:
    """
    draw = ImageDraw.Draw(image)  # draw对象实现在image上绘画
    font_file = os.path.join('Mono.ttf')  # 选定字体文件
    font = ImageFont.truetype(font_file, size=font_size)  # 确定字体和大小
    temp = []
    for i in range(count):
        random_char = random_str()
        draw.text((10 + i * 30, -2), random_char, random_color(),
                  font=font)  # 将字体代入随机字符写入draw文件
        temp.append(random_char)

    valid_str = ''.join(temp)  # 得到生成的字符串，生成された文字列お取得する
    return valid_str, image


# 制造噪点，随机画几条线，随机画几个点
def noise(image, width=120, height=35, line_count=3, point_count=20):
    draw = ImageDraw.Draw(image)
    for i in range(line_count):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)  # 获取两个点的坐标
        draw.line((x1, y1, x2, y2), fill=random_color())  # 在两点之间画线

        # 画点
        for i in range(point_count):
            draw.point([random.randint(0, width),
                        random.randint(0, height)],
                       fill=random_color())
            # 画圆弧
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())
    return image


# 将图片转为base64编码的图片
def valid_code():
    """
    生成图片验证码，并对图片进行base64编码
    """
    image = generate_picture()
    valid_str, image = draw_str(44, image, 35)
    image = noise(image)

    # 调用一个二级制输入流
    f = BytesIO()
    image.save(f, 'png')  # 将图片存入二进制输入流
    data = f.getvalue()
    f.close()

    encode_data = base64.b64encode(data)  # 对data进行编码
    data = str(encode_data, encoding='utf-8')  # 将编码后的数据存入data
    img_data = 'data:image/jpeg;base64,{data}'.format(data=data)
    return valid_str, img_data


if __name__ == '__main__':
    print(valid_code())
