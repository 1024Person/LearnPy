import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    def load_image(self, is_boss):
        self.image = []
        image = 0
        if not is_boss:
            self.blood = 3  # 敌机的血量
            for i in range(1, 6):
                name_image = '../IMAGE/aline{}.bmp'.format(i)
                image = pygame.image.load(name_image)
                self.image.append(image)
        else:
            self.blood = 15  # boss的血量
            for i in range(1, 8):
                name_image = '../IMAGE/boss_{}.bmp'.format(i)
                image = pygame.image.load(name_image)
                self.image.append(image)
        self.rect = image.get_rect()

    def __init__(self, ai_setting, screen, is_boss=False):
        super().__init__()
        self.num = 0  # 规定好贴出的帧数是什么样的

        self.screen = screen
        self.ai_setting = ai_setting
        self.load_image(is_boss)  # 加载敌方飞机的图片

        #   随机生成敌方飞机
        self.centerx = float(randint(0, ai_setting.screen_width))
        self.rect.centerx = self.centerx
        self.centery = float(0)
        # 展示外星人

    def show_alien(self):
        self.screen.blit(self.image[0],self.rect)

    # 外星人的移动路径
    def update(self, ship, setting):
        self.centery += setting.aline_speed_y
        if self.rect.left < ship.rect.left:
            self.centerx += setting.aline_speed_x
        elif self.rect.left > ship.rect.left:
            self.centerx -= setting.aline_speed_x
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
