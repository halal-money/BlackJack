import pygame.display
from settings import *


class Alert:
    def __init__(self):
        self.surface = pygame.surface.Surface((ALERT_WIDTH, ALERT_HEIGHT))
        self.rect = self.surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.display_surface = pygame.display.get_surface()

        # display balance text
        self.font = pygame.font.SysFont('bald', 90)  # choosing a font and size
        self.alert_text = "Your Balance:"
        self.alert_color = (255, 255, 255)  # color of the alert
        self.alert_surface = self.font.render(self.alert_text, True, self.alert_color)
        self.alert_rect = self.alert_surface.get_rect(center=(WINDOW_WIDTH / 2, 215))   # position of the alert text

        # display chip img
        self.chip = pygame.image.load('img/chips/500-chip.png')
        self.chip_size = pygame.transform.scale(self.chip, (150, 150))  # size of the loaded img
        self.chip_rect = self.chip.get_rect(center=(780, 570))  # position of the img

        # display cash balance
        self.balance_text = "$2500"     # initial user balance
        self.balance_color = (255, 255, 255)  # color of the balance text
        self.balance_surface = self.font.render(self.balance_text, True, self.balance_color)
        self.balance_rect = self.alert_surface.get_rect(center=(720, 580))  # position of the balance

    def run(self):
        self.surface.fill((69, 69, 69))
        self.display_surface.blit(self.surface, self.rect)  # display surface (box)
        self.display_surface.blit(self.alert_surface, self.alert_rect)  # display text "Your Balance"
        self.display_surface.blit(self.chip_size, self.chip_rect)   # display 500 chip
        self.display_surface.blit(self.balance_surface, self.balance_rect)  # display user balance
