# 不可变  可变
# 对象指向的内存的值是否能改变
#　int tuple string 是不可变对象
#      int num = 10
#		num = 6 ------>只是改变了num的指向(或者说把标签num贴到另一个地址上了)，
num = 6
print(id(num))
num = 10
print(id(num))

# 可变的   对象指向的内存中的值可以改变

list1 = [1,2,3,4,5,6,7,8,9]
print(list1,id(list1))
list1.pop()
print(list1,id(list1))
dict1 = {}
dict1['123'] = 123
