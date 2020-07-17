# dictionary 字典不允许键重复 允许值重复
dict1 = {} # 空字典
dict2 = {'貂蝉':('梦魇之牙','蓝宝石','蓝buffet')}
print(dict2)
print(dict2)
dict3 = dict([('ID','123456748596'),('name','lucy')])
print(dict3)

dict4 =dict([(1,2),(4,5),(5,5)])
print(dict4)

# 列表转字典 列表中必须两两一队，否则不能转字典

# 记住一个人得注册信息，用一个字典存储一个人得信息

dict6 = {}
dict6["brand"] ='huawei'
print (dict6)
dict6['brand'] = 'mi'

print(dict6)  # 通过键修改值：

# 没有得key则添加到字典中
# dict6[key] = val
# 如果key不在字典中则创建，有则覆盖
dict6['color'] = 'yellow'
print(dict6)


