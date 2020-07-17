'''name = input('')	# 标准输入流，堵塞式,回车表示结束，name容器表示接受容器 

print(name)			# 标准输出流
print('类型：',type(name)) 

# input输出的任何都是字符串


name = input('请输入名字：') # 有提示

print(name)
'''


'''
练习：捕鱼达人

'''

print('''
***********************
      	捕鱼达人
***********************
	''')
user_name = input('输入你的用户名:')
user_password = input('输入你的密码:')


print('亲爱的%s玩家，充值才能游戏' %userName)

coins = input('  请充值')
# int(coins)  只在这一句起作用，下面coins还是字符串类型

print('%s充值成功！当前游戏币%d\n  祝您游戏愉快！'%(userName,int(coins)))

