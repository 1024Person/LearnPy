# def book(**kyagrs):
#     with open('1.txt', 'w') as stream:
#         for key, val in kyagrs.items():
#             code = '{},{}\n'.format(key, val)
#             stream.write(code)
#
#
# book(lucy=('斗罗大陆', '斗破苍穹', '伏天氏'), tom=('元尊',))
#
#
# def read_book(filename):
#     with open(filename) as stream:
#         container_inner = stream.read()
#         print(container_inner)
#     return container_inner
#
#
# container = read_book('1.txt')
#
# print(container)
# print(type(container))
# bookname = []
# start = 0
# while True:
#     index = container.find('\n',start)
#     index_ = container.find(',',start,index)
#
#     bookname.append(container[start:index_:])
#     bookname.append(container[index_+1:index])
#     if index == -1:
#         break
#
#     start = index + 1
# d  = {}
# num = len(bookname)//2
# for i in range(0,len(bookname),2):
#     d[bookname[i]] = bookname[i+1]
# print(d)
#
#
# book =[]
# book.append()

# container = dict(list(container))

# 字符串是不可变序列，，所以不能通过下边进行赋值改变
# book_name = []
# get_book('1.txt')
import random

is_login = False
username = ''  # 账号和密码可以不记录，但是用户名必须记录，因为在后面还要有各种打招呼


# 生成账号
def generate_count():
    count = ''
    for i in range(10):
        ran = random.randint(0, 9)
        count += str(ran)
    return count


# 捐赠书籍
def donate_book(path):
    # book = input('请输入要捐赠的书籍的名称：')
    pass


# 注册账号
def register():
    global is_login
    global username
    try:

        user_name = input('请输入用户名：')
        password = input('请输入密码：')
        pass_word = input('确认密码：')
        count = generate_count()
        if user_name == '':
            # 如果什么都不输入结果是空字符串，，因为用input进行输入的时候，解释器会自动将最后的换行符丢掉
            # 这类似于c语言的gets，输入一行，最后丢掉换行符
            raise Exception
        elif pass_word == '' and password == '':
            raise Exception

        with open('user.txt', 'a') as fp:
            fp.write('count:{}\tusername:{}\tpassword:{}\n'.format(count, username, password))

        if password == pass_word:
            username = user_name
            answer = input("""
            注册成功！
             亲爱的的{}同学,您的账号为{}
             是否要现在登录(yes/no)？""".format(username, count))
            if answer == 'yes':
                login()
        else:
            print('两次密码不一致，注册失败')
    except Exception:
        print('用户名和密码不能为空，注册失败')

    # 登录函数


def login():
    """
    登录函数改变登录状态，改变用户名
    :return:
    """
    global is_login
    global username
    count = input('请输入账号：')
    password = input('请输入密码：')
    try:  # 捕捉一下异常，如果是第一次使用，而且还是没有注册就登陆。那样就会打开失败
        with open('user.txt') as fp:
            lines = fp.readlines()
            for line in lines:
                count_ = line[line.find(':') + 1:line.find(':') + 11:]
                password_ = line[-2:line.rfind(':'):-1]
                if count == count_ and password == password_[::-1]:
                    print('登录成功')
                    is_login = True
                    start = len('count:{}\tusername:')
                    username = line[start:line.find('\t', start)]
                    break
            else:
                print('登录失败T_T.....，账号或密码错误')
    except FileNotFoundError as err:
        print('账号不存在！！！(✖人✖)')


# 查看书籍
def search():
    """
    作用：展示图书目录
    无返回值
    """
    if is_login:
        print('欢迎{}同学，好好学习，天天向上哦 (｡♥ᴗ♥｡) ')
    with open('book.txt') as stream:
        lines = stream.readlines()
        for line in lines:
            print(line)


# 还书
def revert():
    pass


# 借书
def borrow():
    pass


# 开始界面菜单
def menu():
    while True:
        print('=' * 10 + '欢迎来到博智图书馆' + '=' * 10)
        print('\t\t------------------------------------------')
        print('\t\t|        1、注册账号                   |')
        print('\t\t|         2、登录账户                  |')
        print('\t\t|         3、浏览书籍                  |')
        print('\t\t|         4、离开图书馆              |')
        print('\t\t------------------------------------------')
        choice = input('请输入：')
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            search()
        elif choice == '4':
            break
        else:
            print('输入错误，请重新输入！')


menu()
