# 赋值运算符 ‘=’ , 从右向左，将123的值取出（返回一份拷贝），然后赋值给name
# 注意python的赋值运算符就是指向的改变，不是在原先的内存上进行改变，而是改变变量的名字的指向
# python中每一个东西都是地址

name = '123'
name1 = name
# identiy
name1 = '456'	# 注意这个和指针，引用还是有很大的区别的，
print(id(name),'name')
print(id(name1),'name1')
# 重新赋值，指向改变，也就是这个变量是另一个地址的别名
name = '456'
print (id(name),name)
# 直接赋值的就是类的浅拷贝，赋值的地址，
# 变量的名字就是给地址起别名
# python中无论哪一种类型都是类

print(name)
name = 123
name1=name
print(id(name),'name')
print(id(name1),'name1')

# += , -= , *= , /=扩展的运算符
# +=会根据上下文来判断要进行的操作（就是运算符重载）
num = 9
num += 5
print(num)
num *= 5
print(num)


a = 'asd'
b = 'wdc'
a += b		# ‘ += ’ 连接符
print(a)
# a -= b	# ‘-=’ 没有重载
a *= 5		# 重复字符串五次

print(a)
