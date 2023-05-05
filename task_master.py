#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"服务器代码"

__author__ = "BanishedWay"

import random
import time
import queue
from multiprocessing.managers import BaseManager

# 创建发送任务和接收结果的队列
task_queue = queue.Queue()
result_queue = queue.Queue()


def send_task_queue():
    return task_queue


def recieve_result_queue():
    return result_queue


class QueueManager(BaseManager):
    pass


# 将两个Queue注册到网上，callable参数关联Queue对象
QueueManager.register('get_task_queue', callable=send_task_queue)
QueueManager.register('get_result_queue', callable=recieve_result_queue)

if __name__ == '__main__':
    # 绑定端口
    manager = QueueManager(address=('', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 在一台机器上进行操作时，可以直接使用创建的Queue，但是在分布式机器中，必须调用manager.get_task_queue才能调用
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 100)
        print('Put task %d...' % n)
        task.put(n)
    # 从result中读取结果
    for i in range(10):
        r = result.get(timeout=10)
        print('Result:%s' % r)
    # 关闭连接
    manager.shutdown()
    print('master exit')
