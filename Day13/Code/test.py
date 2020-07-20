# 匿名函数
# 定义一个非常简单的函数
# return a + b
# 代码比较少

x = lambda m, n: m + n  # x相当于函数名
print(x(1, 2))  # 输出函数返回值


def add(x, y, func):
    print(x)
    print(y)
    print(func)
    result = func(x, y)
    print(result)


add(1, 5, lambda a, b: a + b)
