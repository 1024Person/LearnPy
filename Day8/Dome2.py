'''
用户注册
密码：
手机号：


'''

users = []

while True:
	print("==="*20)
	print(' '*10,'欢迎来到智联银行')
	username = input('输入用户名:')
	password = input('输入你的密码：')
	repassword = input('再次输入密码：')
	emial = input('输入邮箱：')
	phone = input('请输入手机号：')
	if password != repassword:
		print('两次密码不一致')
		continue
	else:
		user = {}
		user['username'] = username
		user['emial'] = emial
		user['password'] = password
		user['phone'] = phone

		users.append(user)
		answer = input('是否继续注册：(y/n)?')
		if answer == 'n':
			break
		else:
			pass
for user in users:
	print(user)
input('')