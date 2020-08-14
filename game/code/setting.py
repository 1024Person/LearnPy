from time import time


class Setting:
    def __init__(self):
        self.screen_width = 500  # 设置屏幕宽度
        self.screen_height = 700  # 设置屏幕高度
        self.bg_color = 70, 70, 70  # 设置背景颜色
        self.ship_speed_factor_base = 1  # 飞船的初始速度
        self.ship_speed_factor = 1  # 飞船速度
        self.bullet_speed_factor = 1.5  # 设置子弹速度
        self.bullet_width_base = 10  # 设置子弹宽度
        self.bullet_width = self.bullet_width_base
        # 游戏中动态变化的子弹宽度
        self.bullet_height = 30  # 设置子弹高度
        self.bullet_color = 50, 50, 50  # 设置子弹颜色
        self.bullet_num = 3  # 允许同时出现在屏幕中子弹的个数
        self.alien_speed_factor = 0.3  # 敌机的速度
        self.alien_speed_base = 0.3  # 敌机的基础速度
        self.enemy_start = time()  # 敌机出现开始的时间
        self.interval_base = 1  # 敌机出现的基础时间间隔
        self.interval = 1  # 敌机出现的时间间隔
        self.enemy_end = self.interval + self.enemy_start
        self.alien_score_base = 500  # 每个外星人的基础分数
        self.alien_score = 500  # 每射杀一个外星人所获的的分数
        self.experience_base = 100  # 刚开始升一级需要的分数
        self.experience = 100  # 现在升一级需要的经验值

    def update_game(self, stats):
        # 随着玩家等级的提示敌机出现的越来越快，
        # 外星人的分数也越来越高
        # 外星人出现的时间间隔也越来越短
        if self.alien_speed_base * stats.level < 1.2:
            self.alien_speed_factor = stats.level / 2 * self.alien_speed_base

        self.alien_score = stats.level * self.alien_score_base
        if self.interval >= 0.7:
            self.interval -= 0.1
        if self.bullet_width < 150:
            # 设置子弹宽度
            self.bullet_width += stats.level * self.bullet_width_base
        if self.ship_speed_factor < 1.2:
            self.ship_speed_factor += \
                stats.level / 10 * self.ship_speed_factor_base
        # 升一级所需要的分数值
        self.experience *= 2
