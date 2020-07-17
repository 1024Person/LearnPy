# 字典中通过键来当索引
list1 = [1,2,3,54,2,54,12]
print(list1[2])

dict2 = {1:'zhangsan',2:'lici'}
print(dict2)

# 遍历字典
for i in dict2: #获取键
	print(i)
# 字典得函数：
# items() values()  keys
print(dict2.items()) # [(1, 'zhangsan'), (2, 'lici')]
# 返回列表，列表中包含着元组
for i in dict2.items():
	print(i)
for key,val in dict2.items():   # 拆包
	if val == 'zhangsan':
		print(dict2[key])
