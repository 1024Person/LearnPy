# 魔术方法

#   __new__()触发时机：实例化的时候触发的

import sys


class Person:
    def __init__(self, name):
        self.name = name
        print('------------->init')

    #   __new__实例化对象的时候调用 ,而且还必须返回super(Person,cls).__new__(cls)
    #   __new__的作用就是向内存要空间，然后将申请来的内存返回给self，self就存在地址了，
    #   __new__一般不用
    def __new__(cls, *args, **kwargs):
        print('------------>new')
        return super(Person, cls).__new__(cls)

    #   魔术方法：call如果想把对象当做函数使用的话就会触发这个魔术方法
    def __call__(self, *args, **kwargs):
        print('-------------->call')

    #   魔术方法：魔术析构,
    #   触发时机：当没有标签贴在这里的时候就会调用del将所有的内存释放、
    #   自己一般不写以为自己写的话会出现各种内存泄漏，就像C++中的动态申请内存那样
    #   释放不干净
    def __del__(self):
        print('--------->del')

    #   很常用，如果不重写__str__，直接打印对象名，输出的是对象的地址，
    #   如果重写的话就会在打印对象名的时候会，将__str__返回的值也打印出来
    #   __魔术方法：普通方法要调用才会触发，但是魔术方法是自动触发，调用的术方法
    #   魔术方法__str__一定要有返回值，不添加返回值一点意义都没有，而且还会报错
    def __str__(self):
        return '对象的姓名'+self.name


p = Person('Jack')  # 调用了__new__,但是有没有调用__init__呢？
# print(p.name)   #   报错，有__new__的类
print(p)  # p = None
# p()  # 触发魔术方法
# p1 = p
# del p1
# print(p.name)
# print(sys.getrefcount(p))
# del p
# print('p')
