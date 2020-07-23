#   类和类之间的关系-------------------->继承
#   继承的目的之一：减少重复的代码，抽象出公共的部分
#   从一些类中抽象出公共的部分
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        msg = '{}今年{}岁了'.format(self.name, self.age)
        return msg

    def eat(self):
        print('{}正在吃饭'.format(self.name))

    def run(self):
        print('{}正在锻炼身体'.format(self.name))


class Student(Person):
    pass


class Doctor(Person):
    pass


class Worker(Person):
    pass


#   子类中什么都没有，但是调用了父类的__init__(self,name,age)
#   说明一下子类继承父类之后，子类有什么特殊之处：
#       子类继承父类之后，调用方法，首先会在子类中找，
#       如果子类中没有，那么就会到父类中查找这个方法，
stu = Student('小明', 18)
print(stu)
d = Doctor('医生', 25)
print(d)
w = Worker('工人', 40)
print(w)
