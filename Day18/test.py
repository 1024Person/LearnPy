# __all__ = ['add', 'number']
#
#
# def add(*args):
#     if len(args) > 1:
#         s = sum(args)
#         return s
#     else:
#         return 0
#
#
# def minue(*args):
#     if len(args) > 1:
#         result = args[0]
#         for i in args:
#             result -= i
#         return result
#     else:
#         return 0
#
#
# number = 0
#
#
# class Calcuator:
#     def show(self):
#         print('---------------------')
#
#
# if __name__ == '__main__':
#     def test():
#         print('我是测试')
#
#
#     test()

from article.module import Article

a = Article('标题党', 'Uc')
from usr.module import User

u = User('颖宝', '123456')
u.login()