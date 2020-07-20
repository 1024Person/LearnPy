# 登录

islogin = False


def login():
    username = input('输入用户名：')
    password = input('输入密码：')
    if username == '颖宝' and password == '123456':
        return True
    else:
        return False


def is_login(func):
    def wrapper(*args, **kyargs):
        global islogin
        if islogin:
            func(*args, **kyargs)
        else:
            print('用户还没有登录，请先登录')
            islogin = login()
            if islogin:
                func(*args, **kyargs)
            else:
                print("密码或用户名错误，支付失败！")

    return wrapper


@is_login
def pay(money):
    print('支付成功，付款金额为{}'.format(money))


dollar = int(input('请输入支付金额：'))
pay(dollar)
