# 定义函数完成随机数的产生
import random

# 加载函数


def generate_random():

    # 产生10个随机数
    for i in range(1,20):
        i = random.randint(1,20)
        print(i, end=' ')


# 函数名加括号表示调用------>找到函数执行函数体
# 加上括号表示调用，底层到这个内存里面照这个函数
print(type(generate_random))
generate_random()
