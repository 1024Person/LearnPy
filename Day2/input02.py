'''
王者荣耀：
	英雄：xxx
	位置：xxx
	拥有的装备：xxx
	购买装备：xxx
	付款金额;xxx

	xxx拥有了xxx装备，花费了xxx资金

'''

print('''
***********************
	王者荣耀
***********************
	''')
role = input('角色：')
pos  = input('位置：')
equipment = input('输入拥有的装备：')
upgrade_equipment = input('输入想要升级的装备：')
pay = input('输入付款金额:')

equipment =upgrade_equipment

hero = '''
{},占位{},拥有{}装备，
  购买此装备花费了{}钱
'''.format(role,pos,equipment,pay)

print(hero)



