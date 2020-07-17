
# 集合得去重和排序		：
list1 = [12,12,5,20,52,5,2,5,25]
print(list1)
print(set(list1))
list1 = list(set(list1))
# 集合外层是花括号 {}
# 里面都是一个
s1 = set()	# 创建集合只能用这种形式
s1.add('小猪佩奇')
s1.add('lucy')
s1.add('adss')
# add 随机存储
t1 = ('林志玲','jafoi1','dfsa')
#s1.add(t1)
print(s1)
s1.update(t1)
print(s1)


# 删除 remove
s1.remove('林志玲')
print(s1)
s1.pop()
print(s1)
(s1.discard())
print(s1)
s1.clear()
print(s1)