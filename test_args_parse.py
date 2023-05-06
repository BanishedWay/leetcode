#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"测试argparse"

__author__ = "BanishedWay"

import argparse


def main():
    # 定义一个ArgumentParser实例
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL',
        epilog='Written by BanishedWay'  # 说明信息
    )
    # 定义位置参数
    parser.add_argument('outfile')
    # 定义关键字参数
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='3306', type=int)  # 限制类型
    parser.add_argument('-u', '--user', required=True)  # 允许简写
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False,
                        help='Compress backup files by gz')  # gz不跟参数，因此指定actions='store_true'

    # 解析参数
    args = parser.parse_args()
    # 打印参数
    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')


if __name__ == '__main__':
    main()
