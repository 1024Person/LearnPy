#	绘制散点图
#	单词 scatter：scatter   --  撒播；散开；散布；
#		label   ----   标题


import matplotlib.pyplot as plt

# plt.scatter(2,4)	# 向scatter传递一个点，
# y = [0 , 1, 4 , 9 , 16 , 25]
x = list(range(1001))
y = [n ** 2 for n in x]  # 利用列表生成式，得出y列表
# 参数列表：x,y,s,c,alpha,marker,linewidths,
#	edgecolors,cmap,norm,vmin,vimax,verts
# c = y --->根据y列表的值来映射，cmap = plt.cm.Reds   ----->表明映射颜色为红色
plt.scatter(x, y, s=40, c=y, cmap=plt.cm.Reds, alpha=0.5, edgecolors='none')

plt.title('Square Numbers', fontsize=24)

plt.xlabel('Value', fontsize=15)
plt.ylabel('Square of Value', fontsize=15)
plt.axis([0, 1001, 0, 1100000])  # 设置x轴和y轴的取值范围
plt.tick_params(axis='both', labelsize=14)

# 每一个可视化数据都需要一个show来展示
# plt.show()
# 将图表保存到本地,如果想要保存到本地，就不能在这之前调用show，那样的话，会将缓存区中的数据读取到屏幕上去，就没法在保存到本地了
# 而且如果图片的文件名子和本地的文件名重名的话，就会将本地的文件覆盖掉
plt.savefig('1.jpg', bbox_chaes='tight')
