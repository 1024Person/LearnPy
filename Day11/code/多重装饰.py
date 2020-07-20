# 多层装饰
# 离得最近的那个装饰器优先使用哪个装饰器，
# 将第一层装饰完的house传递给第二层装饰器
# 然后通过第二层装饰器的装饰后
# 再将装饰后的函数返回个house


def decorate1(func):
    print('------->1start')

    def wrapper(*args, **kyargs):
        print('刷漆')
        func(*args, **kyargs)

    print('-------->1end')
    return wrapper


def decorate2(func):
    print('-------------->2start')

    def wrapper(*args, **kyargs):
        print('铺地板，装门......')
        func(*args, **kyargs)

    print('------------->2end')
    return wrapper


@decorate2
@decorate1
def house():
    print('我是一个草坯房')


house()
