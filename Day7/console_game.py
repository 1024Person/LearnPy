
import random
heroes = ['鲁班', '后羿','嫦娥','李白','上官婉儿']		# 可选的英雄列表
print('=' * 50)		
print('\t欢迎来到王者荣耀')
print('=' * 50)
while True:											# choice hero
	role = input('请选择英雄：\n1、鲁班 2、后羿 3、嫦娥 4、李白 5、上官婉儿\n')
	if role not in heroes:							# if not
		print('{}不在可选英雄之列，请重新选择'.format(role))
	else:											# is right
		break
coins = 1000										# initialize coins

# weapons library
weapons = [['无尽之刃',2100],['巫师法杖',1980],['回蓝宝石',300],['吸血之刃',1700],['梦魇之牙',2200],['生命宝石',300],['名刀司命',2800]]

equipments = []	# my equipments

print('欢迎，{0}来到王者峡谷，当前金币为{1}'.format(role,coins))

while True:
	# geme mian circulation
	print('-'*40)
	choice = input('请选择:\n1、购买武器\n2、攻击\n3、丢弃武器\n4、查看武器\n5、退出游戏\n选择:')
	if choice.isdigit():	# if input is digit ，then change it type form string to int 
		choice = int(choice)
	if choice == 1:			# buy weapon
		print('欢迎进入武器库:')
		for weapon in weapons:
			print(weapon[0],weapon[1],sep='\t')
		weapon_name = input('请输入要购买的武器:')
		if weapon_name not in equipments:		# now you don't have this weapon
			for weapon in weapons:				# and this weapon in weapon library
				if weapon_name == weapon[0]:	# find this weapon's price
					if coins >= weapon[1]:
						coins -= weapon[1]
						equipments.append(weapon[0])
						print('购买成功，玩家{}当前剩余金币:{}'.format(role,coins))
						break
					else:
						print('金币不足，赶快打仗赚金币吧')	
						break
			else:							# if this weapon don't in weapon library
				print('武器库中没有该武器')
		else:								# if your equipment own this weapon,then don't allow to buy again
			print('武器库中的该武器已经卖光了！！')

	elif choice == 2:						# start war
		if equipments:
			#
			print('进入战场......')
			print('{}拥有的武器如下'.format(role))
			for weapon in equipments:
				print(weapon)
			while True:						# select weapon to attck enemy
				weapon_name = input('请选择：')

				if weapon_name not in equipments:
					print('你的装备中没有该武器，请重新选择！')
				else:
					print('全军出击！......')
					# randint creat ran1 and ran2,if ran1 >=ran2 player win ,otherwise '张飞' win
					ran1 = random.randint(1,20)
					ran2 = random.randint(1,15)
					if ran1 >= ran2:
						print('此局对战，{}获胜'.format(role))
						coins+=300
						print('赚的金币300，此时金币{}'.format(coins))
					else :
						print('此局对战，张飞胜')
					break
		else:
			print('你还没有武器，快去买武器吧！')
	elif choice ==4:
		if equipments:	# if eqipment don't be empty
			print('{}拥有的武器如下'.format(role))
			for weapon in equipments:
				print(weapon)
		else:			# otherwise
			print('{}还没有武器'.format(role))
	elif choice ==3:
		
		print('武器太沉，扔几个')
		if equipments:	# if eqipment don't be empty
			print('{}拥有的武器如下:'.format(role))
			for weapon in equipments:
				print(weapon)
			
			while True:
				weapon_name = input('请选择要删除的武器名：')
				if weapon_name not in equipments:
					print('武器名称输入有误!')
				else:
					equipments.remove(weapon_name)
					
					for weapon in weapons:		# get weapon's price
						if weapon_name in weapon:
							coins += weapon[1]
							break				# add coins
					print('删除成功,当前剩余金币:{}'.format(coins))

					answer = input('是否继续删除？（yes/no）')
					if answer == 'no':
						break
		else:
			print('你都没有武器还沉啥？快去买吧')

			# quit game
	elif choice == 5:
		answer = input('确定离开游戏吗？(yes/no)')
		if answer == 'yes':
			break
	else:
		print('输入错误，请重新选择！')