#   游戏的函数库
import pygame
import sys
from code.bullet import Bullet
from code.enemy import Alien
from time import time


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


def check_play_button(stats, mouse_x, mouse_y, play_button,
                      aliens, bullets, ship, scoreboard):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and \
            not stats.game_active:
        stats.reset_stats(scoreboard)
        stats.level = 1  # 重新设置等级为1
        scoreboard.prep_level()  # 重新生成等级图片
        stats.game_active = True
        # 清空子弹和外星人编组
        aliens.empty()
        bullets.empty()
        ship.rect.centerx = ship.screen_rect.centerx
        pygame.mouse.set_visible(False)


def check_event(ship, ai_setting, screen, bullets,
                stats, play_button, aliens, scoreboard):
    """
    相应事件，如果玩家点了退出游戏则程序结束
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, mouse_x, mouse_y,
                              play_button, aliens, bullets, ship, scoreboard)
            # 如果是按键响应，且按下键盘
        elif event.type == pygame.KEYDOWN:
            check_event_keydown(event, ship, ai_setting, screen, bullets)
            return True

            # 松开键盘
        elif event.type == pygame.KEYUP:
            check_event_keyup(event, ship)
        else:
            return False


def update_screen(screen, setting, ship, bullets, enemys,
                  button, stats, scoreboard):
    screen.fill(setting.bg_color)

    ship.show_ship()
    # 在刷新之前将子弹的图片贴出来
    for enemy in enemys.sprites():
        enemy.show_alien()
    for bullet in bullets.sprites():
        bullet.show_bullet()
    ship.show_ship()
    if not stats.game_active:
        button.show_button()
    scoreboard.show_score()
    scoreboard.show_level()

    pygame.display.flip()


def update_bullet(bullets, enemys, scoreboard):
    """
    更新和子弹有关的数据：坐标，数量
    :param bullets:
    :return:
    """
    bullets.update()  # 更新子弹坐标
    if pygame.sprite.groupcollide(bullets, enemys, True, True):
        scoreboard.stats.score += scoreboard.ai_setting.alien_score
    scoreboard.prep_score()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


# 感觉敌机这一部分应该开一个线程的，
# 玩着玩着游戏就变得慢了
def generate(aliens, ai_setting, screen):
    ai_setting.enemy_start = time()  # 获取当前时间，
    # 并且判断是否应该再次生成一个敌机，可惜自己还不会用计时器
    if ai_setting.enemy_start >= ai_setting.enemy_end:
        # 将start重新赋值为end
        ai_setting.enemy_start = ai_setting.enemy_end
        ai_setting.enemy_end += ai_setting.interval  # end+1
        new_alien = Alien(ai_setting, screen)  # 生成一个敌机
        aliens.add(new_alien)  # 添加到队列中去


def update_enemy(aliens, ai_setting, screen, ship, stats, scoreboard):
    aliens.update()  # 更新敌机的坐标
    update_alien(aliens, ship, stats, scoreboard)  # 判断游戏输赢
    generate(aliens, ai_setting, screen)  # 判断是否生成一个敌机


# 发射子弹
def fire_bullet(bullets, ai_setting, screen, ship):
    if len(bullets) < ai_setting.bullet_num:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def update_alien(aliens, ship, stats, scoreboard):
    """
    游戏结束，判断ship和aliens是否相撞
    如果有敌机出界，等同于和飞机相撞
    :param aliens:
    :param ship:
    :return:
    """
    if pygame.sprite.spritecollideany(ship, aliens) and \
            stats.life >= 0:  # 判断是否相撞
        stats.game_active = False
        scoreboard.stats.reset_stats(scoreboard)
        # stats.game_active = False
    elif pygame.sprite.spritecollideany(ship, aliens) and \
            stats.life < 0:
        print('游戏失败')
        sys.exit()
    for alien in aliens:  # 判断是否越界
        if alien.rect.top > alien.ai_setting.screen_height and \
                stats.life >= 0:
            stats.game_active = False
            scoreboard.stats.reset_stats(scoreboard)
            # stats.game_active = False
        elif alien.rect.top > alien.ai_setting.screen_height and \
                stats.life < 0:
            print('游戏失败')
            sys.exit()


#   判断玩家是否升级
def up_grade(scoreboard):
    if scoreboard.stats.score / scoreboard.ai_setting.experience >= 1:
        scoreboard.stats.level += 1
        scoreboard.prep_level()
        # 更新游戏设计
        scoreboard.ai_setting.update_game(scoreboard.stats)
