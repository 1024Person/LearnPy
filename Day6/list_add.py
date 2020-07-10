# 列表的添加
# 临时的小数据库：
girls = ['颖宝']


# while True:

# 	name = input('请输入你心目中的女神(输入\'q\'退出)：')
# 	if name == 'q':
# 		break
# # 列表的拼接,添加内容
# # append insert extends
# #  追加	  
# # append 末尾追加
# 	girls.append(name)
# print(girls)

# extend 把一个列表添加到另一个列表中，

name = '小月月'
print(list(name))
girls.extend(name)	# 这里就是把name强转为list,然后将后面的那个列表链接到前面
print(girls)




names = ['黑嘉嘉','孙俪','巩俐','王丽坤']
# girls.extend(names)		# 将两个列表合并
# print(girls)

girls+=names
print(girls)



# index 返回索引下标
print(girls.index('黑嘉嘉'))
# insert 指定位置插入
girls.insert(1,'迪丽热巴')
print(girls)

print('-'*40)
import random
random_list = []
for i in range(10):
	ran = random.randint(1,20)
	random_list.append(ran)
print(random_list)
print('-'*40)
random_list = []

i = 0
while i<10:
	ran = random.randint(1,20)
	if ran not in random_list:
		random_list.append(ran)
		continue
	i+=1
print(random_list)

# 系统提供的
print('-'*40)
# 找出最大值
print('最大值:{}'.format(max(random_list)))
# 找出最小值
print('最小值:{}'.format(min(random_list)))

print('-'*40)
max_val = random_list[0]
min_val = random_list[0]
for i in random_list:
	if i > max_val:
		max_val = i
	if i <min_val:
		min_val = i
print('最大值：',max_val)
print('最小值：',min_val)

print('-'*40)
# reverse 默认为False----->升序
# reverse = Ture --------->降序===成绩单
print('排序后的列表\n{}'.format(sorted(random_list,reverse = True)))
# 