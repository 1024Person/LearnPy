# 删除文件夹下的所有文件
# import os
#
# path = os.getcwd()
# path = os.path.join(path, 'Node')
# filelist = os.listdir(path)
# for file in filelist:
#     path1 = os.path.join(path,file)
#     if os.path.isdir(path):
#         continue
#     os.remove(path1)
# print("成功删除所有文件！")
# # os.remove()

# 创建文件夹
# import os
#
# path = os.getcwd()
# path = os.path.join(path, 'Node', '123','456')
# os.mkdir(path)
# print('8'*20)

# 删除所有文件
import os

isright = False


def login():
    """
    登录之后才可以删除，权限设置
    :return:
    """
    global isright
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == '颖宝' and password == '123456':
        isright = True
    else:
        print('密码或账户名错误', end='，')


def decorate(func):
    """

    :param func: 函数
    :return:返回装饰器
    """
    def wrapper(*agrs, **kyagrs):
        if isright:
            func(*agrs, **kyagrs)
        else:
            login()
            if isright:
                func(*agrs, **kyagrs)

    return wrapper


@decorate
def del_all(path):
    """

    :param path: 要删除的目录
    :return: 无
    """
    filelist = os.listdir(path)
    for file in filelist:
        path1 = os.path.join(path, file)
        if os.path.isdir(path1):
            del_all(path1)
            os.rmdir(path1)
        else:
            os.remove(path1)
    os.rmdir(path)

def delete_(path):
    """

    :param path: 要删除地目录
    :return: 无
    """
    del_all(path)
    if isright:
        print('删除成功')
    else:
        print("删除失败")


def delete():
    path = os.getcwd()
    name = os.path.abspath(__file__)
    name = os.path.split(name)
    print(name)
    while True:
        print('='*40)
        filelist = os.listdir(path)
        for file in filelist:
            if file == name[1]:
                continue
            print(file, end=' ,')
        print('\n请从上里面的列表中选择要删除的文件:', end=' ')
        name = input('')
        if name in filelist:
            name = os.path.join(path, name)
            delete_(name)
            answer = input('是否继续删除(yes/no)?')
            if answer == 'no':
                break
        else:
            print('输入错误，请重新输入！')


delete()
