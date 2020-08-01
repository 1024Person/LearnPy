import re

#   match方法，从头开始匹配，完全匹配或者包含
#   两种匹配方法
#   先生成pattern规则，再匹配
msg = '代斯佟丽娅娜扎佟丽娅'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)
print(result)

#   直接匹配
result = re.match('佟丽娅', msg)
print(result)

#   使用search
result = re.search('佟丽娅', msg)
print(result)  # 返回的是出现的区间，只匹配一次
print(result.span())  # span出现的位置,返回值为元组

#   使用group来提取到匹配的内容部分
print(result.group())
print(result.groups())

#   从msg中提取出前面是字母后面是字母中间是数字
msg = 'abcd1f1el4456l5ll6'

#   正则的符号，[]表示的是一个范围：0-9，a-z，A-Z
#   注意[]只占一个位置
#   search只能匹配一次
result = re.search('[a-z][0-9][a-z][0-9]', msg)
print(result)
print(result.group())

result = re.findall('[a-z][0-9][a-z]', msg)  # 其实findall没有那么神奇，因为会有交叉重复的字符串，就比如像上面的那样，
#                                                             a5h6，这个字符串应该是两个符合要求的，但是只会返回一个a5h
print(result)

#   匹配，两边是字母，中间是若干数字的字串

#   正则符号:出现次数有关符号
#   {}  *   +   正则验证中的次数
#   *         有或者没有都行
#   +       至少出现一次
#   ？      要么不出现，要么只出现一次
#   {m}       {m}    用于验证前面的匹配模式匹配m次
#   {m,}       用于验证前面的匹配模式至少匹配m次
#   {m,n}   验证前面的匹配模式至少匹配m次，至多匹配n次
#   +   跟在谁后面就是修饰谁
result = re.findall('[a-z][0-9]+[a-z]', msg)
print(result)

#   正则符号：^    $     卡死符号
#   ^       表示以该符号后面的字符开头
#   $       表示以该符号前面的字符结尾
#   正则表达式严格匹配^和$之间的字符
#   验证qq号码  开头不能是0，qq号码位数5-10
qq = '12345689'
result = re.match('[1-9][0-9]{4,10}$', qq)  # $符号表示严格匹配
print(result)

print('=' * 40)
username = 'admin1&2'
#   当字符串中有特殊字符的时候，就会匹配错误，会匹配到特殊字符的位置就结束了，
#   但是显示匹配成功了，所以这里要加上$符号进行卡死
result = re.match('[a-zA-Z][a-zA-Z0-9]{5,}', username)

#   卡死符号($,^)一般用于search方法
#   卡死符号  (^)  的另一个用法,在[]里面有^符号代表取反
print(result)

#   正则表达式的转义字符
#   '\d'表示的是匹配数字字符
#   ‘\D'表示匹配非数字字符
#   ’\w‘
#   '\W'
#   '\s'
#   '\S'
#
#   用正则表达式匹配出电话号码
#
print('=' * 40)
phone = '19861128635'
result = re.match(r'[1-9][0-9]{9}[0-35689]', phone)
print(result)
print(result.group())  # 通过group提取出来提取出一个出来

#   分组
print('==' * 40)
phone = '101-12345678'
#   用小括号进行分组，提取分组中的内容
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result.groups()[1])  # 提取出两个出来，返回值为元组的形式
print(result.group(1))  # group要配合分组使用

#   引用匹配
print("==" * 25)
msg = '<html>hello</html>'
msg1 = '<html><h1>abc</h1></html>'
#   引用第一个和第二个来匹配，实现提取内容
result = re.match(r'<(html)><(h1)>(.+)</\2></\1>', msg1)

print(result.group(3))

#   给标签取名字  ,注意后面的引用部分也要加上小括号，但是后面的小括号里面的不是子模式
result = re.match(r'<(?P<name1>.+)><(?P<name2>.+)>(.+)</(?P=name2)></(?P=name1)>', msg1)
#      re.math返回的是一个math对象，所以这样就可以调用math对象的方法，比如group方法

print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

#   sub方法
print('==' * 30)
#   直接替换法，写死了
result = re.sub(r'\d+', '100', 'C++:1,python:2')
print(result)


#   函数替换法
def func(temp):
    temp = int(temp.group())
    rest = temp + 1
    return str(rest)


result = re.sub(r'\d+', func, 'java:98,python:99')
print(result)

#   前片操作
result = re.split('[,:]', 'java:98,python:100')
print(result)