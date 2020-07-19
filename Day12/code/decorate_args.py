"""
带参装饰器是三层的，
    最外层的是用来接受装饰器的参数的
    中间层的是用过来接受被装饰的函数的
    最内层的使用来接受被装饰函数的参数的



"""


def outer(s):  # 首先，从从最外层接收参数
    def decorate(func): # 第二层，接收函数值
        def warrper(*args, **kyargs):   # 内部函数接受被装饰的函数的参数
            func(*args, **kyargs)
            print('铺地板{}块'.format(s))

        return warrper  # 返回内部函数

    return decorate # 返回装饰器


@outer(10)
def house():
    print("我是一个草坯房")


house()
