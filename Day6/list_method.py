names = ['Tom','Jack','Jack+Tom','Lucy','钢铁侠']
names_=names
print(names)
print(names[::-1])

names[-1] = 'ironman'
print(names[::-1])

print('-'*40)
# 这里的name和C++中的for循环for(auto i:vec)中的i差不多只能遍历不能改变
for name in names:
	if 'ironman' == name:
		name = '钢铁侠'
else:
	print(names)

'''
# 边删除边遍历，结果就是i越界
print('-' *40)
for i in range(len(names)):
	if names[i] == 'ironman':
		names[i] = '钢铁侠'
else:
	print(names[::-1])
print('-' * 40)
del names[1]
print(names)
print('-'*40)
for i in range(len(names)):
	if names[i] == 'ironman' or names[i] == 'Tom':
		del names[i]
print(names)



# for circulation range only run one
print('*' * 40)
l = len(names)
for i in range(l):
	if names[i] == '钢铁侠' or names[i] == 'Tom':
		del names[i]
		l-=1
print(names)
'''
print('-'*40)
l = len(names)
i = 0
while i < l:
	if names[i] == 'ironman':
		del names[i]
		l-=1
	i+=1
print(names)

print('-'*40)

# 注意下面的name 和 names_的地址！！！发生了浅拷贝，
if id(names) == id(names_):
	print('names的地址和names_的地址相同，发生了浅拷贝！！！')
names = names_
i = 0
while i < len(names):
	if 'Jack'in names[i]:
		del names[i]
		print('Jack在里面')
		continue
	i+=1


