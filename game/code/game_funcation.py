#   游戏的函数库
import pygame
import sys
from code.bullet import Bullet


def check_event_keydown(event, ship, ai_setting, screen, bullets):
    """

    :param event:
    :param ship:
    :param ai_setting:
    :param screen:
    :param bullets:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
        # 如果按下了空格键，
        # 并且屏幕中的子弹数量没有超标生成一颗子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_setting, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_event_keyup(event, ship):
    """
    如果键盘松开
    :param event:监听到的事件
    :param ship: 飞船
    :return: None
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_event(ship, ai_setting, screen, bullets):
    """
    相应事件，如果玩家点了退出游戏则程序结束
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            # 如果是按键响应，且按下键盘
        elif event.type == pygame.KEYDOWN:
            print(ship.rect)
            check_event_keydown(event, ship, ai_setting, screen, bullets)
            print(ship.moving_left,ship.moving_right,ship.moving_up,ship.moving_down)
            # 松开键盘
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, ship)


def update_screen(screen, setting, ship, bullets, alien):
    screen.fill(setting.bg_color)
    ship.show_ship()
    # 在刷新之前将子弹的图片贴出来
    for bullet in bullets.sprites():
        bullet.show_bullet()
    alien.show_alien()
    pygame.display.flip()


def update_bullet(bullets):
    """
    更新和子弹有关的数据：坐标，数量
    :param bullets:
    :return:
    """
    bullets.update()  # 更新子弹坐标
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


# 发射子弹
def fire_bullet(bullets, ai_setting, screen, ship):
    if len(bullets) < ai_setting.bullet_num:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)
