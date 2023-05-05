#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"分布式机器代码"

__author__ = "BanishedWay"

import time
import sys
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 这里只需要接收，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server = '127.0.0.1'

if __name__ == '__main__':
    # 端口和验证码必须与设定的一致
    m = QueueManager(address=(server, 5000), authkey=b'abc')
    m.connect()

    # 获取对象
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 从task队列读取任务，并写入result
    for i in range(10):
        n = task.get(timeout=1)
        print('run task %d * %d' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    print('work over')
