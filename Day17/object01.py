class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return '这个人的名字叫做{},他今年{}岁了'.format(self.name, self.__age)

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


p1 = Person('牛逼', 19)
print(p1)
print(dir(p1))
# print(p1._Person__age)  # 不推荐的访问私有属性

#   __name__的用法
# def test():
#     print(__name__)
