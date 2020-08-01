class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.islogin = False

    def __str__(self):
        msg = '''
            用户名：{}
            密码：{}
        '''.format(self.__username, self.__password)
        return msg

    def login(self):
        username = input('输入用户名：')
        password = input('输入密码：')
        if self.__username == username and password == self.__password:
            print('登录成功')
            self.islogin = True
        else:
            print('登录失败')


if __name__ == '__main__':
    u = User('颖宝', '123456')
    print(u)
    u.login()
