# 闭包
# 在函数中定义的，就是返回一个函数指针
# 闭包的特点：将内部函数扔出来

"""
闭包的条件：
    1、在外部函数定义了一个内部函数
    2、有返回值
    3、返回的是一个内部函数
    4、内部函数还引用了一个外部函数的变量值
"""


def func(a, b):
    c = 100

    def inner_func():
        s = a + b + c
        print('相加之后的结果为', s)

    return inner_func


# add 就是内部函数，相当于函数指针
add = func(10, 200.252)
add()

