#   多继承的顺序
#   obj.__mro__
#   import inspect
#   inspect.mor
#   多继承主要就是了解继承的顺序，和查找顺序

class A:
    def __init__(self):
        self.name = 'A'

    def show(self):
        print('-----------------A')


class B:
    def show(self):
        print('---------------------B')


class C1(A, B):
    pass


class C2(A, B):
    def show(self):
        print('------------C2')


class D(C1, C2):
    pass

# c = C()
# c.show()
# print(C.__mro__)  # 先找C中有没有show，没有的话就找A，如果A也没有再找B
#   python中的多继承，就像是树结构中的按一行一行的进行查找，
#   叫做广度优先搜索
d = D()
d.show()
print(D.__mro__)