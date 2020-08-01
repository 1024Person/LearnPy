import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load("../IMAGE/alien.bmp")
        self.rect = self.image.get_rect()

    # 展示外星人
    def show_alien(self):
        pass

    # 外星人的移动路径
    def update(self):
        pass
    
