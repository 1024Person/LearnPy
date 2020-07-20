# 闭包的简单应用
# 打破壁垒，（打破作用域的权限）
# 记录状态


def func(a, b):
    c = 100

    def inner_func():
        s = a + b + c
        print('相加之后的结果为', s)

    return inner_func


# add 就是内部函数，相当于函数指针
a = 120
b = 123

add = func(a, b)
add1 = func(1, 2)

add()  # a , b 状态下的相加
add1()  # 1,2 状态下的相加
# 闭包不会因为参数的改变而受影响

f = func

print(f(1, 2))
print(add1)
print(add)
f(1, 2)()
