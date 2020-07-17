# for i in range(1,50,5):
# #	print(i)
# i = 0
# while i<= 12:
# 	print(i)
# n = 1
# sum = 0
# while n <= 20:
# 	sum += n
# 	n += 1

# print('',sum)
# del sum
# print(sum(range(21)))


#嵌套循环
#----------------------
#打印直角三角形

#打印杨辉三角

#----------------------

# for i in range(1,5): # py特有的
# 	print('*' * i)
# i = 10
# while i >= 1: # 通用的嵌套循环
# 	j = i
# 	while j >= 1:
# 		print('*',end = '')
# 		j -= 1
# 	print('')
# 	i -= 1
# 打印杨辉三角





#'''
#---------------------------
#九九乘法表
#--------------------------
#'''
for i in range(1,10):
	j = 1
	print('-' * i * 9)
	while j <= i:
		print('{}x{} = {} |'.format(i,j,i*j),end = ' ' ) 
		j += 1

	print()
# '''
# ----------------------

# 练习：
# 循环猜数

# '''
pay = 5
print('-'*30)
money = 0
print('*'*10,'欢迎进入澳门皇家赌场','*'*10)
username = input('请输入用户名：')
answer = input('确定进入游戏吗？(y/n)')
if answer == 'y':
	while money < 2:
		print('-'*30)
		n = int(input('余额不足，请充值之后再继续玩\n充值金额（30个币一百块钱，必须是100的倍数）：'))
		if n % 100 == 0 and n > 0:
			money = (n // 100) * 30 
		else :
			print('充值失败！30个币一百块钱，充值金额必须是100的倍数')
	print('充值成功，当前游戏币：{}\n每局游戏销毁{}个币'.format(money,pay))	
# 开始游戏
	while True:
		print('-'*30)
		if money - pay <= 0:			# 判断余额是否充足
			answer = input('尊敬的{}用户，您的余额为{}币，不足以玩这这局游戏，是否充值后继续游戏？(y/n)'.format(username,money))
			if answer =='n':
				print('欢迎下次光临,再见')
				break
			elif answer == 'y':
				print('请到前台充值，')
				break
			else :
				print('输入错误！')
				break
		import random
		t1 = random.randint(1,6)
		t2 = random.randint(1,6)

		print('洗牌完毕，进入游戏............')
		money -= 5										# 减游戏币
		guss = input('请输入大或者小:')					#玩家猜大小
		if t1+t2>6 and guss == '大' or t1 + t2 <=6 and guss == '小':
			print('恭喜{}，猜对了，游戏币加 1 '.format(username))
			money += 1
		else :
			print('真遗憾，猜错了')
		answer = ('还继续游戏吗？(y/n)')
		if answer == 'n':
			break
		