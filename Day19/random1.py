import random

ran = random.random()  # 0-到1之间的随机小数
print(ran)

print(random.randrange(1, 10, 2))  # 产生一定范围的随机数，并且结合步长
#   randrange如果不传步长，就是random.randint
print(random.randint(1, 10))

l = ['颖宝', '123', '456', '7898']
print(random.choice(l))  # 从给定的列表中随机选出一个元素，

pai = ['红桃', '方片', '梅花', '黑桃']
random.shuffle(pai)  # 将列表中的元素顺序打乱，洗牌方法
print(pai)


def func():
    code = ''
    for i in range(4):
        ran1 = chr(random.randint(65, 90))
        ran2 = chr(random.randint(48, 57))
        ran3 = chr(random.randint(97, 122))
        c = random.choice([ran1, ran2, ran3])
        print(c)
        code += c
    return code


code = func()
print(code)

print(ord('上'))  # 汉字的编码值
print(chr(19978))  # 编码转字符
print(ord('下'))
print(chr(19979))