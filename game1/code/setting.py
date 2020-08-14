class Setting:
    def __init__(self):
        self.screen_width = 500  # 设置屏幕宽度
        self.screen_height = 700  # 设置屏幕高度
        self.bg_color = 80, 80, 80  # 设置背景颜色
        self.ship_speed_factor = 1.5  # 飞船速度
        self.bullet_speed_factor = 1  # 设置子弹速度
        self.bullet_width = 3  # 设置子弹宽度
        self.bullet_height = 15  # 设置子弹高度
        self.bullet_color = 50, 50, 50  # 设置子弹颜色
        self.bullet_num = 3  # 允许同时出现在屏幕中子弹的个数
        self.aline_speed_y = 0.1  # 地方飞机的x的速度
        self.aline_speed_x = 0.1  # 外星人飞机的y速度
