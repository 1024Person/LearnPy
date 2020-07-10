# 基本结构
# print(range(6)) # 包含开始，不包含结束（stop） （begin，stop，step）
# range(50,5) ---------->结果没有


# for i in range(30):
# 	print('\thello ----------->',i)


# print('---------------game over------------')



'''
-----------------------
吃五个馒头
	这五个馒头中有一个是毒馒头，
	第三个馒头上摸了鹤顶红
-----------------------
'''
# name = '小明'

# for i in range(1,6):
# 	if i == 3 :
# 		print('小明快把第{}个馒头扔了，有剧毒"{}"'.format(i,'鹤顶红'))
# 	else:
# 		print('{}很饿，正在吃第{}个馒头'.format(name,i))
# print('{}终于吃饱了'.format(name))

''' 
----------------------------
	for和else进行匹配
for……else……（else可选可不选）
for正常结束的时候就会进入else
break强制跳出循环，直接跳到else后面
break不会进入else，
else和for是一体的
pass空语句，直接通过
再不确定要写什么的代码的时候，先占位，直接通过
为了保证语法的完整性

'''
# if 1 < 0:
# 	print('888')
# else:
# 	print('*******')
# print('---------------')

# for i in range(3):
# 	print('*' * 30)
# 	username = input('请输入用户名：')
# 	password = input('请输入密码：')
# 	if username == 'admin' and password == '123456':
# 		print('欢迎用户:{},登陆成功：'.format(username)	)
# 		print('---------轻松购物吧----------')
# 		break
# 	else:
# 		print('用户或密码错误')
# else:
# 	print('密码错误次数超过3次，账号已被锁定')
# 	# pass

print('\aadf\f')