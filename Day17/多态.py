#   python中没有严格的多态，因为python是一种弱类型的语言，无法限制传参的类型
#   但是python中还是存在多态，主要是因为isinstance这一个函数
#   这个函数的严格表示是：如果是这个类的对象或者是这个类的子类对象，结果为真

class Pet:
    role = '宠物'


class Dog(Pet):
    role = '狗'

    def eat(self):
        print('{}正在吃东西'.format(self.role))


class Cat(Pet):
    def eat(self):
        print('{}想吃东西'.format(self.role))


class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):
        if isinstance(pet, Pet):
            print('{}养了一只宠物{}'.format(self.name, pet.role))
        else:
            print('这不是宠物，不能养')


class Tiger:
    def __init__(self, name):
        self.name = name


cat = Cat()

dog = Dog()

p = Person('xxxx')
p.feed_pet(cat)
p.feed_pet(dog)

print('=====================')

tiger= Tiger('黑心虎')
p.feed_pet(tiger)

