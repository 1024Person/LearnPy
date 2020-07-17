# 元组  tuple   ()小括号
# 元组中的内容不可修改

t = ()
print(type(t))
t =(1)
print(type(t))
t = (1,)  # 元组中只有一个数据的在一个数据之前还要放
import random
list1 = []
for i in range(10):
	ran = random.randint(1,10)
	list1.append(ran)
print(list1)
print(tuple(list1))

t5 = tuple(list1)
print(t5[-1])
print(t5[6:4:-1])  # 切除出来的是元组


'''
元组得符号()
不可变序列：
元组得运算符
'''

t2  = (4,5) + (56,56)
print(t2)
print(t2 is t5)

print(len(t5))
print(max(t5))
print(min(t5))
print(sum(t5))
print(sorted(t5))		# sorted 函数排序之后返回得是一个列表
print(tuple(sorted(t5)))   
