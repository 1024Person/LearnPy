#   集合推导式和列表推导式差不多，
#

set1 = {n + 1 for n in range(10) if n % 2 == 1}
set2 = {n + 100 if n > 100 else n + 300 for n in range(10)}
print(set1)
print(set2)

#   字典推导式：字典推导式要符合字典中元素的形式
#   反转字典中的键和值
dict1 = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'c'}
dict2 = {value: key for key, value in dict1.items()}
print(dict2)