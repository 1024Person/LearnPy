# list1 = [1,2,3,45,12,1,2]
# s1 = set()	# 声明只能是set()
# 			# set的特点无序不重复
# s2 = {}		# s2是字典
# 			# 字典里面放的都是键值对
# 			# 集合里面放的是一个一个存在的

# print(type(s2))
# s3 = set(list1) # set的作用：去重和排序  
# print(s3)


# # set的增删改查

# # 增
# # add 方法：
# s1.add(1)
# s1.add('小猪佩奇')
# print(s1)
# # update方法
# t1 = ('林志玲志玲姐姐','言承旭')
# s1.update(t1)	# 将t1给拆了  
# print(s1)
# s1.add(t1)		# add是将整个都添加进去
# print(s1)	

# # 删

# s1.remove('言承旭')
# print(s1)
# # s1.remove('姐姐')
# # print(s1)
# s1.pop()		# pop删除的是第一个
# print(s1)

# s1.discard('姐姐')	#和remove类似，但是没有的话不会报错
# print(s1)

# s1.clear()		# 清空
# print(s1)

# set1 = {1,2,3,8,1,52,85,1,8552}
# print(set1)
# num = int(input('输入一个数字：'))

# set1.discard(num)
# print(set1)

print('=='*20)
set1 = {1,2,3,8,1,52,85,1,8552}
# 运算符操作
print(6 not in set1)
set2 = {1,2,3}
print(set1 == set2)				#set1 和 set2是两个不同的地址
print(set1 is set2)				#内容相等

print(set1 != set2)

# set3 = set1 + set2
# print(set3)
# set3 = set1 * 2
# print(set3)

set4 = set1 - set2 				# 减号是差集 difference
print(set4)

set5 = set1.difference(set2)	# 找不同，就是差集
print(set5)

# & 交集	 共同拥有的 intersection
set6 = set1 & set2
print(set6)

set7 = set1.intersection(set2)
print(set7)

# union 并集
set8 = set1.union(set2)
print(set8)