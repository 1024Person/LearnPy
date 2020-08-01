# 非堵塞式进程池
#   进程池是为了防止请求进程过多导致系统崩溃
"""
"""
import os
from multiprocessing import Pool
from time import sleep, time
from random import random


def task(task_name):
    start = time()
    print('做任务{}'.format(task_name))
    sleep(random() * 2)
    end = time()
    print('完成任务{},用时{},进程id:{}'.format(task_name, end - start, os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['学py', '学C++', '学编程', '赚钱', '买山地车', '减肥']
    for taski in tasks:
        pool.apply_async(task, args=(taski,))
    pool.close()
    pool.join()

    print('over!!!!!!')
#   皮卡丘背景图
