import pygame.display
from settings import *
from button import Button
from chips import chips_dict


class Chips:
    def __init__(self):
        self.surface = pygame.surface.Surface((410, 200))
        self.rect = self.surface.get_rect(bottomleft=(190, 650))
        self.display_surface = pygame.display.get_surface()

        # display chips
        self.twenty_five = Button(button=chips_dict['25'], btn_size=(100, 100), btn_rect=(190, 650))

        self.fifty = Button(button=chips_dict['50'], btn_size=(100, 100), btn_rect=(290, 650))

        self.hundred = Button(button=chips_dict['100'], btn_size=(100, 100), btn_rect=(395, 650))

        self.five_hundred = Button(button=chips_dict['500'], btn_size=(100, 100), btn_rect=(500, 650))

    def run(self):
        # self.display_surface.blit(self.surface, self.rect)
        self.display_surface.blit(self.twenty_five.button_size, self.twenty_five.rect)
        self.display_surface.blit(self.fifty.button_size, self.fifty.rect)
        self.display_surface.blit(self.hundred.button_size, self.hundred.rect)
        self.display_surface.blit(self.five_hundred.button_size, self.five_hundred.rect)

