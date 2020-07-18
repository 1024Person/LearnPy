# 可变参数
# 注意：可变参数可以放在前面，但是可变参数的后一个参数必须显示指明参数的值，比如end=‘/n’
# 但是最好还是将可变参数的值放在后面，而且但是放在后面好像只能放一个可变参数


def add(*agrs, name):
    # 可变参数是元组
    sum = 0
    if len(agrs) == 0:
        print('{}没有可以计算的值,sum = {}'.format(name, sum))
    else:
        for i in agrs:
            sum += i
        print('{}计算的结果为{}'.format(name, sum))


add(1, 1, 2, 34, 1, name='周深')
