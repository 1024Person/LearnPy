from multiprocessing import Process
from time import sleep
from random import random


class Myprocess(Process):
    def run(self):
        n = 1
        while True:
            print('进程名字：{}'.format(self.name))
            n += 1
            print(n)
            sleep(random() * 2)
            if n >= 10:
                break

    def __init__(self, name):
        super().__init__()
        self.name = name


if __name__ == '__main__':
    myprocess = Myprocess('进程一')
    myprocess.start()

#   进程一旦被唤醒就会指向run函数
