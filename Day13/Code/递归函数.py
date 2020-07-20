# 函数种类：普通函数,匿名函数，递归函数
# 递归函数：函数自己调用自己

"""
1、用递归求累加和


"""


def sum(n):
    """
    文档说明
    :param n:
    :return:
    """
    if n == 1:
        return 1
    else:
        return sum(n - 1) + n

result = sum(10)
print(result)


