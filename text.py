from settings import *


class Text:
    def __init__(self, text, color):
        self.text = text
        self.text_color = color  # color of the text
        self.font = pygame.font.SysFont('bald', 120)  # font and size
        self.surface = self.font.render(self.text, True, self.text_color)
        self.rect = self.surface.get_rect(center=(WINDOW_WIDTH / 2, 215))
