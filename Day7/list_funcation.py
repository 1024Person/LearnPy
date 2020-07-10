# 列表对象的成员函数
# 添加：append extend insert
# 删除：remove dle pop clear

hotpot_list = ['海底捞','热辣一号','宽板凳']

hotpot_list.append('张良麻辣烫')

#print(hotpot_list)
# 只删除第一个匹配成功的，如果找不到的话就是返回异常
#result = hotpot_list.remove('杨国福麻辣烫')

#print(hotpot_list)

#print(result)

print('-' * 40)

# pop 弹栈	返回值为删除的元素
# 弹栈就是返回操作，栈结构
reuslt = hotpot_list.pop()

print(reuslt)

print(hotpot_list)

print('-'*40)

hotpot_list.insert(1,'张良麻辣烫')
# 可以指定index删除，如果不指定就是最后一个(-1)
result = hotpot_list.pop(2)

print(hotpot_list)

print('-'* 40)
print('reverse:',end = ' ')
hotpot_list.reverse()		# 直接倒序改变了源字符串
print(hotpot_list)


print('-'* 40)
print('clear:',end = ' ')
hotpot_list.clear()
print(hotpot_list)

print('-'*40)
print('list.sort:')
l = [12,5,3,65,23465,1245]
# 默认是升序，
# reverse False------> 升序
# reverse True-------> 降序
l.sort()
print(l)
l.sort(reverse = True)
print(l)



print('='*40)
print(l.count(65))












