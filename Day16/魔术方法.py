# 构造方法：init也叫初始化的方法，

class Person:
    def __init__(self, name, age):  # 魔术方法还可以传参，
        """
        魔术方法中就是添加对象的属性，一般在这里添加所有对象的共同属性，
        而且，这个初始化函数和C++中的构造函数还有点不一样，C++的构造函数可没有增加对象属性这一功能
        这主要源于python语言的弱类型的特点

        """
        self.name = name
        self.age = age
        #   而且可以发现，在方法中，所有与对象有关的属性或者另外的方法，基本上都是通过self来实现的

    def eat(self, *food):
        print('{},今年{}岁了,正在吃{}'.format(self.name, self.age, food))


p = Person('王五', 12)
p.eat('大米饭', '红烧肉', '大猪肘子')
