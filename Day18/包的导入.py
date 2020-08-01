from usr import *  # 将整个包导入到程序中，如果没有定义__all__列表的话，包中的所有模块都不能使用，
#                       只有在这个包下面的__init__.py文件中定义一个__all__列表才可以使用__all__列表中所列出的模块
from usr.module import User
#   在导入包的时候，会第一时间加载__init__.py文件中的代码
a = User('颖宝', '123456879')


