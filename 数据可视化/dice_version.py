from dice import Dice
import pygal

dice1 = Dice()
dice2 = Dice()
# dice3 = Dice()
result = []
for i in range(1000000):
    result.append(dice1.roll() * dice2.roll())
frequencies = []
max_result = dice1.dice_side * dice2.dice_side
for i in range(2, max_result + 1):
    frequencies.append(result.count(i))
print(frequencies)
hist = pygal.Bar()  # 创建一个类，Bar的类
hist.title = '筛子结果分析'  # 设置标题
hist.x_title = '点数'  # x的标题
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']  # 设置x轴的数据
# 使用列表推导式推出列表
hist.x_labels = [n for n in
                 range(2, dice1.dice_side * dice2.dice_side
                       + 1)]
hist.y_title = '结果'
hist.add('D%d * D%d'
         % (dice1.dice_side, dice2.dice_side),
         frequencies)  # 设置标签？和一个列表，
# 要显示在y轴上的列表
hist.render_to_file('dice1_version1.svg')
