# find string and replace string
# method : find() rfind() lfind() rinsex() lindex() replace()

s1 = 'transport'
result = 'l' in s1
print(result)
# s2 = 'ASdsadf'
# print(s2.casefold())    # casefold ---->funcation:make every charater字母


postion = s1.find('r')    # return index of find str
while postion != -1:
    print(postion)
    print(s1[postion:])
    postion = s1.find('r',postion + 1,len(s1))
# arguments 参数
# http://it.jhliujj.cn/python1982casde/picture/course-level1.png
url = 'http://it.jhliujj.cn/python1982casde/picture/course-level1.png'

p = url.rfind('/')
file_name = url[p + 1:] 
print(file_name)

p = url.rfind('.')
file_kz = url[p + 1:]
print(file_kz)
# 找不到的话，就会报异常
# p = 'hello'.index('x')
# print(p)
# 
# replace
s1 = 'www.baidu.com'
s2 = s1.replace('.','360')  # 如果不指定第三个参数，那么就是全部替换,
# 第三个参数，指定最多替换多少次
print(s2)