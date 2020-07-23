# class Person:
#     age = int()
#     brithday = str()
#
#     def eat(self,food):
#         print('{}正在吃{}'.format(self.name,food))
#
#
# p = Person()
# p.name = '张三'
#   python的对象中是可以动态添加成员的，
#   也就是说，由于python是一个弱类型语言，赋值就是定义，
#   所以在python中并没禁止单个对象自己添加属性，但是这样就对类的要求更高了，
#   类：所有该类对象的共性，所有对象的交集，在类的方法中只能操作所有对象的共性属性
#       其他的不能进行操作
# p.eat('红烧肉')
# p1 = Person()
# p1.eat('白开水')

#
class Cat:
    type_cls = '猫'

    def __init__(self, name, age, color):
        self.name = name;
        self.age = age
        self.color = color

    @classmethod
    def change_type(cls):

        cls.type_cls = '狗'

    @staticmethod
    def run(self):
        self.name = '123'
        print('快跑')

    def eat(self, *food):
        print('{}喜欢吃{}'.format(self.name, *food))

    def catch_mouse(self, weight, color):
        print('{}捉到了一只{}千克的{}的老鼠'.format(self.name, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('乖乖，继续睡吧！')
        else:
            print('快起床捉老鼠了！')

    def show(self):
        print('姓名：{}\t年龄：{}\t颜色：{}'.format(self.name, self.age, self.color))

# 单个对象的将类属性改变之后，影响不了其他对象的类属性，
#   通过类将类属性改变之后，所有对象的属性都将改变
Cat.change_type()

# Cat.type_cls = 'GOU'  # 在类方法里面改变不了类属性？只能直接通过类点出来才能改变？
cat1 = Cat('Tom', 2, '黄色')
cat2 = Cat('Jack', 3, '黑色')
cat1.catch_mouse(8, '灰色')
cat1.run(cat1)
cat1.show()
cat1.sleep(10)
cat1.eat('煎饼', '大葱', '黄瓜')
# cat1.type_cls = '狗'

print(cat1.type_cls)
print(cat2.type_cls)
