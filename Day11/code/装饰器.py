# 在闭包的基础上的升级就是装饰器

"""
    加入购物车，付款，修改收货地址……
    要求----->用户登陆状态

"""
#
#
# def func():
#     print('-' * 12)
#
#
# def F(f):
#     f()
#     print(f)
#
#
# F(func)
#

"""

 装饰器的特点是：
    1、函数作为参数出现的，作为参数，将函数A作为参数穿给了函数B
    2、要有闭包的特点出现在里面
"""


def decorate(func):
    def wrapper():
        func()
        print('-------->铺地板')
        print('-------->装门')

    return wrapper


# 当house定义完成之后：
# 将house当作参数传递给了，decorate，
# 接着就是调用decorate函数
# 再接着就是将wrapper函数返回
# 然后用house函数进行接受
@decorate
def house():
    print('我是一个茅草屋')


house()  # house指向了wrapper，调用的是wrapper

"""
可以发现上面的装饰器都是只能装饰无参函数，传递参数的时候，
还要在重新改装饰器，
我们可以用可变参数来定义装饰器---------->万能装饰器
万能装饰器：
# def decorate(func):
    def wrapper(*args,**kyargs):    # 装包
        ........
        .........
        func(*agrs,**kyargs)                # 拆包
    return wrapper
"""


def decorate1(func):
    def wrapper(*args, **kyargs):
        func(*args, **kyargs)
        print("==" * 30)

    return wrapper


@decorate1
def func1(students):
    for s in students:
        print(s)


stu = ['Tom', 'Jack', 'Lucy']
func1(stu)


@decorate1
def func2():
    print('这是func2')


func2()

# 通过上面可以总结出一个规律：在定义一个装饰器的时候，
# 最好都写上可变参数和关键字参数
