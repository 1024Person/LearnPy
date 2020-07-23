class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return '{}今年{}岁了，他家住在{}'.format(self.name, self.age, self.address)


class Student(Person):
    pass


class Doctor(Person):
    pass


stu = Student('张贵龙', 20, '临沂市')
print(stu)
