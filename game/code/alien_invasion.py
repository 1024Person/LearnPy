#!\D:\Python
import pygame
from code.setting import Setting
from code.ship import Ship
import code.game_funcation as gf

from pygame.sprite import Group


def run_game():
    """
    初始化游戏并创建一个screen对象（surface对象就是
    游戏中的每一个元素，pygame.init()
    返回的surface是整个屏幕）
    :return:
    """
    setting = Setting()

    pygame.init()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("真的能自学python吗？")
    ship = Ship(screen, setting)
    bullets = Group()
    # 游戏的主循环
    while True:
        gf.check_event(ship, setting, screen, bullets)  # 按键检查
        ship.update()  # 更新飞船的坐标
        gf.update_bullet(bullets) # 更新子弹
        gf.update_screen(screen, setting, ship, bullets)  # 更新画面


run_game()
