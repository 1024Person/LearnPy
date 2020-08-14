from time import time
from pygame import mouse


class Stats:
    def __init__(self, ai_setting):
        self.ai_setting = ai_setting
        self.life = 4
        self.game_active = False
        self.score = 0
        self.level = 1  # 玩家等级

    def reset_stats(self, scoreboard):
        """
        将游戏状态重置
        :return:
        """
        self.score = 0
        self.life -= 1
        self.game_active = False
        self.ai_setting.interval = self.ai_setting.interval_base
        self.ai_setting.enemy_start = time()
        self.ai_setting.enemy_end = \
            self.ai_setting.interval + self.ai_setting.enemy_start
        self.ai_setting.bullet_width = \
            self.ai_setting.bullet_width_base
        self.ai_setting.ship_speed_factor = \
            self.ai_setting.ship_speed_factor_base

        scoreboard.ai_setting.enemy_start = time()
        scoreboard.ai_setting.enemy_end = \
            scoreboard.ai_setting.enemy_start + \
            scoreboard.ai_setting.interval
        scoreboard.ai_setting.experience = \
            scoreboard.ai_setting.experience_base
        scoreboard.prep_level()

        self.ai_setting.alien_speed_factor = \
            self.ai_setting.alien_speed_base
        self.ai_setting.alien_score = self.ai_setting.alien_score_base
        mouse.set_visible(True)
