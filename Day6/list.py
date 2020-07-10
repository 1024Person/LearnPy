names = ['Tom','Jack','Lucy','superman','ironman']	# 声明列表
ages=[]
print(id(names))
print(id(names[0]))
print(id('Tom'))	
# 和数组有点不同，列表中第一个元素的地址不是列表的地址

print(id(ages))

# list----> add remove change find

print('-'*40)
print(names[0])
print(names[1])
print(names[-1])
# ages.push(19)
# print(ages[0])

# by len method,get the length of list
print(names[len(names) -1 ])


# method frist
print('-'*40)
for name in names:
	new_str = name[-3:]		# cut the end three character
	if new_str == 'man':
		print('超人在里面')
		break
	else:
		print(name)
else:
	print('超人不在里面')


# method second
print('-'*40)
if 'superman' in names:
	print('超人在里面')
else:
	print('超人不在里面')

# method thrid
print('-' * 40)
msg = '超人在里面' if 'superman' in names else '超人不在里面'
print(msg)



