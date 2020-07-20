import os

isright = False


def login():
    """
    登录函数，权限设置
    :return:
    """
    global isright
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == '颖宝' and password == '123456':
        isright = True
    else:
        print('密码或账户名错误', end='')


def decorate(func):
    """

    :param func:装饰器，判断用户是否登录
    :return:
    """

    def wrapper(*args, **kyargs):
        if isright:
            func(*args, **kyargs)
        else:
            login()
            if isright:
                func(*args, **kyargs)
            else:
                print('用户名或密码错误', end='，')

    return wrapper


def copy(scr, target):
    """

    :param scr: 原路径带文件名
    :param target: 目标路径带文件名
    :return:
    """
    with open(scr, 'rb') as rstream:
        with open(target, 'wb') as wstream:
            wstream.write(rstream.read())


@decorate
def copy_all(scr_path, target_path):
    """

    :param scr_path: 原路径（没有文件名）
    :param target_path: 目标路径（没有文件名）
    :return: 无
    """
    filelist = os.listdir(scr_path)
    for file in filelist:
        path1 = os.path.join(scr_path, file)
        path2 = os.path.join(target_path, file)
        if os.path.isdir(path1):
            os.mkdir(path2)
            copy_all(path1, path2)
        else:
            copy(path1, path2)
    print('复制完毕！')


def printf(path):
    """
    打印该文件夹下的所有文件
    :param path: 要进行打印的文件夹
    :return:
    """
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isdir(file):
            print('\t', end='')
            print('|', file, '----->', end='\t')
            filedir = os.path.join(path, file)  # filedir是文件夹路径，
            printf(filedir)
        else:
            print(file, end='\t')
    print('\n')


path = os.getcwd()
printf(path)
filename1 = input('要复制的文件夹：')
filename2 = input('要复制到的文件夹')
path1 = os.path.join(path, filename1)
path2 = os.path.join(path, filename2)
copy_all(path1, path2)
