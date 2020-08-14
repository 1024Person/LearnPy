from pygame import font


class Scoreboard:
    def __init__(self, screen, stats, ai_setting):
        # 获取保存一些游戏设置
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.ai_setting = ai_setting
        # 显示得分字体时颜色的设置
        self.text_color = (25, 25, 25)
        self.font = font.SysFont(None, 48, True)

        self.prep_score()
        self.prep_level()

    # 准备图片的，因为要将文字转成图片才能贴在屏幕上
    def prep_score(self):
        """
        注：没有标明的image都是分数的image
        :return:
        """
        # 分数的图片生成
        self.stats.score = round(self.stats.score, -1)
        self.score_str = "{:,}".format(self.stats.score)

        self.score_image = self.font.render(self.score_str,
                                            True, self.text_color, self.ai_setting.bg_color)
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def prep_level(self):
        # 等级的图片生成
        self.level_str = str(self.stats.level)
        self.level_image = self.font.render(self.level_str, 48, self.text_color,
                                            self.ai_setting.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)

    def show_level(self):
        self.screen.blit(self.level_image, self.level_image_rect)
