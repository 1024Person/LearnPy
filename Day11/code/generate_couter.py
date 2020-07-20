# 计数器
def generate_counter():
    count = [0]

    def add_one():
        count[0] += 1
        print('这是第{}次访问'.format(count[0]))

    return add_one


counter = generate_counter()
counter()
counter()
counter()

# 通过闭包达到一个静态变量的作用
# 因为同一个返回的函数内部的count的地址是唯一的
# 所以可以通过返回值函数进行修改同一个列表s
