#   如果父类中有__init__()并且子类中也有__init__()
#   如果子类和父类中有同名的方法

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
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # 使用super类调用父类的方法，不仅仅可以调用父类的__init__还可以调用父类的其他方法
        self.salary = salary

    # def __init__(self, salary):  # 没有报错但是，下面标着红色波浪线，表示不规范，
    #     # 因为没有调用父类的__init__()那么一些属性就会不存在，如果在父类中使用了这种属性的话程序就会崩溃
    #     print('--------------->Student的init')
    #     self.salary = salary

    def eat(self, food):    # 在子类中有和父类重名的方法，则先找到子类的方法，然后调用，这种叫做重写
        #   也可以在子类中调用父类方法，如果子类方法依赖于父类的同名方法的话
        super(Student, self).eat()
        print('{}喜欢吃{}'.format(self.name, food))


class Doctor(Person):
    pass


class Worker(Person):
    pass


stu = Student('100', 20, 100000000)
stu.eat('红烧肉')
