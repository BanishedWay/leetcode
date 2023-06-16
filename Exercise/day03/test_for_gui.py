#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"使用GUI编程实现随机密码生成器"

__author__ = "BanishedWay"

import tkinter as tk
import password_generator as pg


def show_input():
    output.delete(1.0, tk.END)
    output.insert(tk.END, pg.get_password(int(input.get())))


def close_windows():
    window.destroy()


if __name__ == '__main__':

    # 主界面
    window = tk.Tk()
    window.title("パスワードジェネレーター")
    window.geometry("300x200")

    # 添加输入框
    input = tk.Entry(window)
    input.pack()

    # 添加生成按钮
    button = tk.Button(window, text="生成", command=show_input)
    button.pack()

    # 添加结束按钮
    button_exit = tk.Button(window, text="出口", command=close_windows)
    button_exit.pack()

    # 添加输出框
    output = tk.Text(window)
    output.pack()

    window.mainloop()
