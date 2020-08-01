from multiprocessing import Process
from time import sleep
import os

n = 1


def task1(s):
    global n
    while True:
        print('-task1', '---->', os.getpid(), '---->', os.getppid())
        sleep(s)
        n += 1
        print(n)


def task2(s):
    global n
    while True:
        print('-task2', '---->', os.getpid(), '---->', os.getppid())
        sleep(s)
        n += 2
        print(n)


if __name__ == '__main__':
    p = Process(target=task1, args=(1,), name='任务1')

    print(p.name)
    p.start()  # 唤醒进程
    p1 = Process(target=task2, args=(1,), name='任务2')
    p1.start()
    print(p1.name)
    n += 1
    print(n)

    #
    # number = 1
    # while True:
    #     number += 1
    #     sleep(0.2)
    #     if number >= 50:
    #         p1.terminate()
    #         p.terminate()
    #         print(number)
    #         break
#   进程的格式：
#       from multiprocessing import Process
#       def func:
#           ……
#       p = Process(……)
#   每一个进程中都有一个独立的全局变量
#   多进程之间没有不能共同访问全局变量
#

#   进程实现多任务同时进行，是并行关系
#   主进程：开启子进程，子进程执行任务，主进程执行下面的任务，
