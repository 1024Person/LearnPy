#   三中导入模块的方式
#   import test ，在使用模块中的东西的时候，前面必须要带上模块的名称
#   from test import add,number     ,从模块中导入一部分，使用的时候，可以不带模块名
#   from test import *      ，将模块中的所有东西都导入到文件中，在使用模块中的东西的时候可以不加模块名
#   但是可以通过__all__来限制*所获得的的内容
import test

result = test.add(1, 2, 3, 4, 5, 6, 7, 8)
print(result)
print(test.number)

from test import number

print(number)

from test import *

print(add(1, 2, 3, 4, 5, 6, 7, 8))
# print(minue(1,2,3,4))   无法直接调用因为在test模块中定义了，__all__=['add','number']

# __name__和__main__
#   用法：在编写模块的时候，经常需要测试模块的性能，
#   所以就会在模块中直接调用已经写好的函数，
#   但是如果在模块中有函数调用的话，就会感觉很突兀，
#   因为模块只是提供函数的，如果突然之间出现一个莫名其妙的函数调用，这很不合理
#   一种方法就是直接删除这段代码，但是如果这段代码，以后还是会用到话就不能删除
#   说这么多，其实__name__ == __main__就是和c++中的# ifndef差不多，预编译的
#   在有__name__的文件中执行程序，那么__name__就是__main__
#   如果在另一个文件中执行程序但是在导入的模块中还有__name__，那么此时__name__就是模块的名字








