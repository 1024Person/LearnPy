#   python中没有重载，只有重写
#   后面的同名函数会把前面的函数覆盖掉，也不存在重定义的问题
class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}吃东西'.format(self.name))

    def eat(self, food):
        print('{}正在吃{}'.format(self.name,food))


p = Person('小明')
p.eat('狮子头哦')