# lambda的更深层次的应用
# map函数
list1 = [1, 2, 3, 5, 2, 636, 2]
# lambda和三目表达式
list2 = list(map(lambda x: x if x % 2 == 0 else x + 1, list1))
print(list2)

# reduce

tuple3 = (1, 2, 3, 5, 8, 7)
from functools import reduce

# reduce 累加，将之前相加的和作为下一次相加的第一个参数，与之后取出的数字进行相加
# reduce 是用来加减乘除的
result = reduce(lambda x, y: x + y, tuple3)
print(result)

# sorted  key

list1 = [{'name': 'tom', 'age': 10}, {'name': 'lucy', 'age': 20}, {'name': 'time', 'age': 25}]

# 用sorted的key时候，还要指明key = ...
result = sorted(list1, key=lambda x: x['age'])
print(result)
result = sorted(list1, key=lambda x: x['age'], reverse=True)
print(result)
