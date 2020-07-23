#   可迭代的一定是迭代器对吗？
#   所有的迭代器都可以用next()调用并且返回元素
#   刚才报了一个警告：因为我是从collections中导入了Iterable，
#   警告说：在python3.3中还可以，但是现在好像已经停止工作了，所以提示我从collections.abc中导入Iterable
from collections.abc import Iterable

g = (n for n in range(10))
print(isinstance(g, Iterable))
list1 = [1, 2, 3, 5, 8]
print(isinstance(list1, Iterable))
print(isinstance(100, Iterable))
#   上面的语句只是证明了迭代性，但是可迭代的不一定是迭代器，
#   迭代器的定义：可以用next内置函数不断地获取元素的叫做迭代器
try:
    next(list1)
except:
    print('列表不是可迭代的')
else:
    print('列表不是可迭代的')
#   列表不是可迭代的对象

list2 = iter(list1)
print(next(list2))

try:
    next(list2)
except Exception as err:
    print('list2不是迭代器')
else:
    print('list2是迭代器')