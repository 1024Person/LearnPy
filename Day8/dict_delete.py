dict1 = {'小为':100,'历次':123,'八次':12}
del dict1['小为']				# 没有的话返回异常
print(dict1)
print(dict1.pop('历次'))			# 只要删除成功了就返会val值
print(dict1.pop('张小三','没找到'))# 没有找到返回默认值：就是第二个参数
print(dict1)
print(dict1.popitem()) 			# 将末尾最后得元素删除
print(dict1.clear())			# 全删除
'''
update
fromkeys(seq[,dafulte])   ---------->将seq转成字典得形式如果没有val值得话就直接得赋值为none


'''
dict1 = {'小为':100,'历次':123,'八次':12}
dict2 = {0:'123',2:'456'}
dict2.update(dict1)
print(dict2)

list1 = ['aa','bb','cc']
print(dict.fromkeys(list1))	
print(list1)