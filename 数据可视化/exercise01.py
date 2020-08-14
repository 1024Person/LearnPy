if __name__ != '__main__':
    from dice import Dice
    import matplotlib.pyplot as plt

    dice = Dice()
    result = []
    output = []  # y轴坐标
    input = []
    for i in range(1000):
        result.append(dice.roll())
    for i in range(1, dice.dice_side + 1):
        output.append(result.count(i))
        input.append(i)
    plt.plot(input, output, linewidth=5)
    plt.show()
if __name__ == '__main__':
    import pygal
    from RandWalk import RandomWalk

    rw = RandomWalk()
    rw.fill_walk()
    hist = pygal.Bar()
    hist.x_labels = [str(n) for n in rw.x]
    hist.add('随机漫步点数', rw.y)
    hist.render_to_file('随机漫步.svg')
