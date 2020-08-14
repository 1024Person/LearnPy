import pygame


class Ship:
    def __init__(self, screen, ai_setting):
        """
        每一个surface都会有一个自己的外接矩形，
        加载进程序的ship.bmp也是一个surface，
        但是ship这个类并不是一个surface对象，
        这个类只不过是想要将image进行维护，
        :param screen: 最大的那个屏幕
        :param ai_setting: setting设置类
        """
        self.ai_setting = ai_setting  # 设置类
        self.screen = screen  # 整个屏幕
        self.image = pygame.image.load('../IMAGE/ship.bmp')
        self.rect = self.image.get_rect()  # rect这个飞船的外界矩形
        self.screen_rect = screen.get_rect()  # 整个屏幕的矩形

        #   让ship出现在屏幕的中间
        #   rect.centerx就是ship的中心   x
        # 整个屏幕的x的中间
        self.rect.centerx = self.screen_rect.centerx
        # 整个屏幕的底部
        self.rect.bottom = self.screen_rect.bottom
        #   保存飞船的精确坐标,精确的x坐标
        self.centerx = float(self.rect.centerx)
        print(self.rect.centery)
        self.centery = float(self.rect.centery)
        # 控制持续移动飞船,刚开始设置为False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def show_ship(self):
        """
        将图片绘制到指定的位置上去，因为是绘制到屏幕上去，
        而pygame初始化的返回结果就存放在了self.screen中，
        所以直接对self.screen操作就可以了
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        #   如果向左向右同时按下
        if self.moving_right and self.moving_left:
            pass
        #   如果上下键同时按下
        elif self.moving_down and self.moving_up:
            pass
        elif self.moving_right and self.is_moving():
            # 如果向右移动为真的话，向右移动速度
            #   中心self.center不是rect.center
            self.centerx += self.ai_setting.ship_speed_factor
            # self.rect.centerx += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.is_moving():
            # 如果向左移动为真的话，就向左移动速度
            self.centerx -= self.ai_setting.ship_speed_factor
            # self.rect.centerx -= self.ai_setting.ship_speed_factor
        elif self.moving_up and self.is_moving():  # 向上移动
            self.centery -= self.ai_setting.ship_speed_factor
            # self.rect.centery -= self.ai_setting.ship_speed_factor
        elif self.moving_down and self.is_moving():  # 向下移动
            self.centery += self.ai_setting.ship_speed_factor
            # self.rect.centery -= self.ai_setting.ship_speed_factor
        else:
            pass
            #   将self.center的值赋值给了self.rect.centerx
            # print(self.rect.centerx, self.rect.centery, self.centerx, self.centery)
            self.rect.centerx = self.centerx
            self.rect.centery = self.centery

    def is_moving(self):
        # 如果向右移动为真的话，
        # right = self.rect.left + self.rect.width
        # screen_right =  self.screen_rect.centerx * 2
        if self.moving_right and \
               self.rect.right < self.screen_rect.right:
            print(self.rect.right, self.rect.left)
            return True
        #   如果向左移动为真的话
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            return True
        elif self.moving_up and self.rect.top \
                < self.screen_rect.top:
            return True
        elif self.moving_down and self.rect.bottom > 0:
            return True
        #   上述条件都不满足，返回值为假
        else:
            return False
