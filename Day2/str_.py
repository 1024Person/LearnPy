'''name ='大白'
print('收件人名字'+name)
age =19
print('年龄是：'+str(age),type(age)) # 拼接的val的类型一定是同等类型的
print('年龄是：%s'% age) # 格式化输出时，底层会进行强转
isMarry = False
print('结婚否？%s',isMarry)

age =1.25
print('年龄' ,(age))
print('年龄%d' % age) # 强转截断
year = 2020
print('今年是%02d' %year)

salary = 99999.258
print('我的薪水：%.1f' % salary) # .1表示小数点后面的位数，而且是四舍五入，
'''

'''
练习：看电影示例
moive = '期末考试'
moive_count = 65
ticket = 25
sum_money = ticket * moive_count

电影名称：期末考试
电影人数:65
电影单价：25
电影总票价：

'''
moive = '期末考试'
moive_count = 65
ticket = 25.99
total = ticket * moive_count

moive_message = '''

电影名称：%s
电影人数:%d
电影单价：%.3f
电影总票价：%.3f
''' % (moive,moive_count,ticket,total)
print(moive_message)

# 现在必须要顶格写，否则的话会报缩进错误