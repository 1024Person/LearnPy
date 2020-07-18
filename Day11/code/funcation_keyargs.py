# 可变参数：关键字参数
# 关键字参数：默认值key = val
# 可变参数，用一个*表示元组的形式，用两个*（**）表示用字典的形式，就是装包，每个参数要用键值对的形式，一传传一对


# def add(a, b=10, c=1, d=10):
#     result = a + b + c + d
#     print(result)
#
#
# add(5)
# add(1, 2)
# 如果是想给c赋值，但是b用默认值，的用法
# 在传参的时候。指明关键字进行赋值,而且在交换位置以及之间的参数上都要指明关键字，没有影响到的可以不用指明关键字
# add(1, c=8, b=10)


# **的可变参数的时候，必须要用关键字传参，关键字作为键，关键字的值作为值，
# 在传参的时候，可以使用**可变参数


def print_perosn(**kwargs):
    # 装包将关键字参数装包成字典的形式
    print(kwargs)


boy = {'123': 0, '456': 456, '789': 789}
print_perosn(**boy)  # 拆包，将字典拆成关键字的形式


# print_person(boy)      # 报错，因为**kwargs只接受关键字参数

# 在参数列表中有*可变参数，还有**可变参数的时候，将*可变参数放在**可变参数的前面
def func(a, b, *agrs, **kwagrs):
    print(a, b, agrs, kwagrs)


func(1, 2)
func(1, 3, 4)
func(1, 2, c=123, d=456)
func(1, 2, 3, c=456)
# func(1, 2, a=789, 1)        #报错，因为如果先对**参数进行传参，那么解释器会认为你已经将中间的那个参数跳过了

