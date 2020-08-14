# 生成多张随机漫步图
from RandWalk import RandomWalk
import matplotlib.pyplot as plt

while True:
    # 调节窗口大小
    plt.figure(figsize=(10, 6))
    rw = RandomWalk()
    rw.fill_walk()
    # 通过point_number设置渐变颜色，来突出显示大致路径
    point_number = list(range(rw.point_num))

    # plt.scatter(rw.x, rw.y, s=10, c=point_number, cmap=plt.cm.Reds)
    plt.plot(rw.x, rw.y, linewidth=3)
    plt.scatter(rw.x[0], rw.y[0], s=100, c='red')
    plt.scatter(rw.x[-1], rw.y[-1], s=100, c='black')
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    yn = input('是否继续')
    if yn == 'n':
        break
