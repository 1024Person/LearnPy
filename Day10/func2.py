# 带参数的函数
# 参数的个数

import random


def generate_random_int(number):
    for i in range(number):
        ran = random.randint(1, 20)
        print(ran, end=' ')


number = int(input('输入要产生的随机数的个数'))
generate_random_int(number)
print('==' * 20)


# 找最大值函数


def max_list(iterator):
    m = iterator[0]
    for i in iterator:
        if m < i:
            m = i
    print('最大值为：', m)


max_list([1, 2, 3, 45, 5, 3485, 32456])
print(isinstance([], list))     # isinstance 判读是不是  #type 看到底是什么类型
