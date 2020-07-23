list1 = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
print(list1)
L = [(n, m) for n in range(5) if n % 2 == 0 for m in range(10) if m % 2 != 0]
print(L)

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 0]]
L = [i[2] for i in L]
print(L)

# 列表推导式：
#   1、带条件的列表推导式
#   2、不带条件的列表推导式
#   3、注意列表推导式中的i
#   4、带else的列表推导式
#   5、三目运算符-----> 表达式1  if 判断 else : 表达式2
#   如果if判断为真，则执行前面的表达式1 否则执行后面的表达式2


#   带有else的列表推导式
dict1 = {'name': 'lucy', 'salary': 8000}
dict2 = {'name': 'tom', 'salary': 7000}
dict3 = {'name': 'jack', 'salary': 3000}
dict4 = {'name': 'array', 'salary': 5000}
dict5 = {'name': 'make', 'salary': 6000}

L = [dict1, dict2, dict3, dict4, dict5]

#   带有else的列表推导式

newlist = [person['salary'] + 100 if person['salary'] > 5000 else person['salary'] + 500 for person in L]
print(newlist)

#   列表推导式的一般形式：[n for n in range(110) if ]      --->后面的if可选可不选，这个推导式从for哪里开始，
#       然后向后走（如果后面还有的话），走到最后再回到最前，将符合条件的元素添加到列表中
#       添加完成之后，再次返回for循环，然后重复上述操作，直到for的判断条件为假时，列表推导式结束
#   总结上面的步骤就是：在列表推导式中，在判断条件为真的时候，
#       语句是循环进行的，就是从for开始，走到最后返回前面
#       注意：判断条件属于for循环，也就是说在for循环后面跟着的if语句是在本层for循环之下的
list1 = [n + m for n in range(10) if n % 3 == 0 for m in range(4) if m % 4 == 0]
