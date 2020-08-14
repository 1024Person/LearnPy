import pygame
from random import randint
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load("../IMAGE/aline1.bmp")
        self.rect = self.image.get_rect()
        self.rect.centerx = randint(0, ai_setting.screen_width)
        self.centery = 0.0

    # 展示外星人
    def show_alien(self):
        self.screen.blit(self.image, self.rect)

    # 外星人的移动路径
    def update(self):
        self.centery += self.ai_setting.alien_speed_factor
        self.rect.centery = float(self.centery)
