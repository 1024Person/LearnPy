import pygame.font


class Button:
    def __init__(self, screen, ai_setting, msg):
        # 保存一些游戏的属性
        self.ai_setting = ai_setting
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 创建一些按钮自己的属性
        self.width, self.height = 200, 50
        self.button_color = 0, 255, 0
        self.text_color = 255, 255, 255
        self.font = pygame.font.SysFont('楷体', 48, True, True)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg = msg
        self.prep_msg()

    def prep_msg(self):
        """
        渲染字体的？
        将字体渲染为图片，并在按钮上居中
        :return:
        """
        self.msg_image = self.font.render(self.msg, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def show_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
