# # 字符串学习
# s1 = 'asdf'
# s2 = "asdf"		# 常量赋值，地址一样
# s3 = '''		
# asdf
# '''

# print('the id of s3:',id(s3),'\nThe id of s2:',id(s2),'\nThe id of s1:',id(s1))


# s1 = input('请输入')		# 键盘输入，input底层改变了
# s2 = input('请输入')

# print('s1 == s2:',s1 == s2)	# ==号比较的是内容
# print('s1 is s2:',s1 is s2)	# is比较的是地址，交互式所见即所得，
# # 内容一样，地址不一定相同，
# # 地址一样，内容一定一样



# string <-----operator
# '+' ----->拼接 
# '*' ----->重复
# 'in' ---->在……里面

name = 'Tom'
result = 'T' in name
print(result)

result = 'tom' not in name
print(result)


# % ----->string format
print('%s shoule hard learn English'%(name))

# r ----->保留原格式
print(r'%s say：\" we should hard learn English\"' % (name))


file_name = 'image.png'
print(file_name[5])		# 通过方括号进行访问，只能获取一个字母
# 切片操作（cut） : ----------> [1:10]
print(file_name[0:5])	#前闭后开		类似range()包前不包后

# 省略：--------->省略后面的就是一直切到结尾
#    ------------>前边省略，表示从零开始取
#    ------------> 负数，-1表示最后一个
print(file_name[:5])
# don't print
print(file_name[2:1])
print(file_name[-1],file_name[8])

print(file_name[:-1])
print(file_name[-1:])

# 倒序输出，::

print(file_name[::-1])	


# 切片的最后一个参数表示方向，正的表示从前向后切，负的表示从后向前
print(file_name[0:5:1])	# 单个切片的最后一个参数的值，表示步长


# hello world
# reverse print :world
# print ：hello
# reverse print ：hello world
# print oll
#

string = 'hello world'
print(string[4::-1],string[5:])
print(string[::-1])
print(string[4:1:-1])
print(string[2:-3])

print(string[::2])
