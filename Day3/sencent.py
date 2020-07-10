# 语句
''' 
if	条件判断语句  
for	循环语句部分 
	跳转语句
if 	elif …… else
条件控制：
	1、登录验证
	2、
python：判断的变量是  空字符串，0 ，None，都默认为False
'''
# username = input()
# #空字符串

# if username:
# 	print('登陆成功')
# 	print('------------------\n\t快买吧')
# else :
# 	print('请稍等')
# num = 90
# if num:
#	print('num :',num)
'''
如果年龄大于18，并且输入了姓名
	对应一个事件

'''
age = int(input('输入年龄：'))
username= input('输入姓名：')

if age >= 18 and username:
	print=('%s 今年，%d岁'% (username, int(age) ))

else :
	print('请烧火')
print('--------------------')
'''
	if :
		事件
	else :
		事件
'''

'''
level 1:
	免费玩
level 2:
	充费在玩
'''
print('*'*10,'欢迎来到消消乐','*'*10)
level = input('请输入你的等级（level 1 or level 2）：')
if level == 'level 1':
	print('免费玩，随便玩')
else:
	print('已进入付费级别，充钱继续玩')
	money = int(input('请充值（必须是100的倍数）'))
	if money % 100== 0 and money > 0:
		print('充值成功，充值金额为：{}'.format(money))
	else:
		print('充值失败，充值金额必须是100的倍数')
print('-'*20)
'''
---------------------------------------
随机数：
import randmo
猜大小
	系统生成一份随机数，
	输入一个数字，
	将系统产生的进行比较，
	如果相等，猜对了，重大奖
	如果不相等，拜拜，下次再来
---------------------------------------
'''
import random

result = random.randint(1,10)
play =int( input('请输入，你猜的数字:') )
if play == result:
	print('恭喜你，中大奖了，试卷一叠')
else :
	print('很遗憾，你与奖品擦肩而过了')

'''
---------------------------------------
百分制分数
多个条件：优秀，良好，及格，待及格
if 表达式：
	…… 
elif 表达式：
	……

……
else
---------------------------------------
'''
'''
猜年龄
'''
age = int(input('请输入，三笠姐姐的年龄：'))

if age <= 18:
	print('太有眼光了，她是你的了，嘿嘿')
elif age >18 and age < 30:
	print('人家还没当妈妈呢……')
elif age >= 30 and age <= 40:
	print('猜的太年轻了')
else :
	print('输入错误！')