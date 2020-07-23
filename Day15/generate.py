#   生成器的构建方式：
#   1、类似列表生成式
#   2、函数加yield关键字构建生成式

#   生成器对象产生元素
#   生成器对象.__next()__
#   内置函数next(生成器对象)

#   生成器对象发送数据send
#   发送的数据在暂停之后，将会替代哪个位置原本该有的数据
g = (i for i in range(10))

print(g.__next__())
print(next(g))


#   函数生成器

def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        a, b = b, b + a
        yield b
        n += 1


g = fib(10)
while True:
    try:
        print(g.__next__(),end='\t')
    except:
        break

