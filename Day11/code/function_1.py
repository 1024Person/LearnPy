# 内部函数
# 在函数的里面又声明了一个函数


def func():
    # 声明变量：
    a = 1000

    list1 = [11, 2, 3, 3]

    def inner_function():
        # 在py中函数的定义和声明是一个概念
        # 或者说在py中没有声明这一个概念
        for index, val in enumerate(list1):
            list1[index] = val + 5
        list1.sort()

    inner_function()
    print(list1)


func()
