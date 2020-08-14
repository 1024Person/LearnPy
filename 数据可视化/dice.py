from random import randint


class Dice:
    def __init__(self, dice_side=6):
        """
        骰子
        :param dice_side:筛子默认是六面
        """
        self.dice_side = dice_side

    def roll(self):
        """
        掷骰子
        :return:返回的是结果的面
        """
        return randint(1, self.dice_side)


if __name__ == '__main__':
    dice = Dice()
    result = []
    for i in range(10000):
        result.append(dice.roll())
    frequencies = []
    for i in range(1, dice.dice_side + 1):
        frequencies.append(result.count(i))
    print(frequencies)
