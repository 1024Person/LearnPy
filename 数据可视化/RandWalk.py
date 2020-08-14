from random import choice


class RandomWalk:
    def __init__(self, point=5000):
        self.point_num = point
        self.x = [0]
        self.y = [0]

    # 填充随机漫步的路径
    def fill_walk(self):

        while len(self.x) < self.point_num:
            dircetion = choice([1, -1])
            x_distance = choice([0, 1, 2, 3])
            x_step = dircetion * x_distance

            dircetion = choice([1, -1])
            y_distance = choice([0, 1, 2, 3])
            y_step = dircetion * y_distance

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x[-1] + x_step
            self.x.append(next_x)
            next_y = self.y[-1] + y_step
            self.y.append(next_y)
