from settings import *


class Button:
    def __init__(self):
        self.button = pygame.image.load('img/start_button.png')     # start_btn img
        self.button_size = pygame.transform.scale(self.button, (250, 200))
        self.rect = self.button_size.get_rect(bottomleft=(320, 600))
        self.surface = pygame.display.get_surface()

    def run(self):
        self.surface.blit(self.button_size, self.rect)
