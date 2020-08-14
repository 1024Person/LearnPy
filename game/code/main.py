"""

还差一个计分系统和一个最高分，等级制度…………
在pdf里面还有很多的东西没有做

"""
import pygame
from code.setting import Setting
from code.ship import Ship
import code.game_funcation as gf
from code.Button import Button
from code.game_stats import Stats
from pygame.sprite import Group
from code.scoreboard import Scoreboard


# 游戏的入口
def main():
    """
    初始化游戏并创建一个screen对象（surface对象就是
    游戏中的每一个元素，pygame.init()
    返回的surface是整个屏幕）
    :return:
    """
    setting = Setting()

    pygame.init()
    screen = pygame.display.set_mode(
        (setting.screen_width, setting.screen_height))
    pygame.display.set_caption("真的能自学python吗？")
    ship = Ship(screen, setting)
    button = Button(screen, setting, 'Play')  # 这里不支持中文
    bullets = Group()
    enemys = Group()
    stats = Stats(setting)
    scoreboard = Scoreboard(screen, stats, setting)
    # 游戏的主循环
    while True:
        gf.check_event(ship, setting, screen, bullets,
                       stats, button, enemys,scoreboard)  # 按键检查
        if stats.game_active:  # 如果游戏处于活动状态才进行下面的操作
            ship.update()  # 更新飞船的坐标
            gf.update_bullet(bullets, enemys, scoreboard)  # 坐标，碰撞，分数
            # 坐标，生成aliens，碰撞，重置
            gf.update_enemy(enemys, setting, screen, ship, stats,
                            scoreboard)
            # 查看是否升级
            gf.up_grade(scoreboard)

        gf.update_screen(screen, setting, ship, bullets,
                         enemys, button, stats, scoreboard)  # 更新画面


if __name__ == '__main__':
    main()
