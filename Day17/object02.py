#   加上装饰器，让私有属性当做共有属性一样用 ，感觉就像是脱裤子放屁自找麻烦
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    # 第一个被property装饰的方法，必须是无参的？？？
    # 下面会报错，必须现有get再有set
    #   报错：TypeError: name() takes 1 positional argument but 2 were given
    # @property
    # def name(self, name):
    #     self.__name = name

    # 下面这样就不会报错了
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


p1 = Person('小白', 19)
p1.name = '大白'
print(p1.name)
print(p1.age)
