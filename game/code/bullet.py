from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        # 获取画面
        self.screen = screen
        # 设置速度
        self.speed = ai_setting.bullet_speed_factor
        # 创建矩形
        self.rect = \
            pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        # 设置位置
        self.top = ship.rect.top
        self.rect.centerx = float(ship.rect.centerx)
        #   设置子弹的纵坐标
        self.y = ship.rect.y
        #   设置子弹的颜色
        self.color = ai_setting.bullet_color

    # 将子弹的位置进行更新
    def update(self):
        self.y -= self.speed
        self.rect.centery = self.y

    def show_bullet(self):
        """
         展示子弹函数
        :return:
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
