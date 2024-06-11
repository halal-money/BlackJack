import os
import random

from settings import *
class Chips:
    def __init__(self):
        self.surface = pygame.surface.Surface((CHIPS_WIDTH, CHIPS_HEIGHT))

        # Creating a dict with chip images and their value
        self.chip_value = {}
        for filename in os.listdir('img/Chips'):
            if filename.startswith('25'):
                image = pygame.image.load(f'img/Chips/{filename}')
                self.chip_value['25'] = image
            elif filename.startswith('500'):
                image = pygame.image.load(f'img/Chips/{filename}')
                self.chip_value['500'] = image
            elif filename.startswith('50'):
                image = pygame.image.load(f'img/Chips/{filename}')
                self.chip_value['50'] = image
            elif filename.startswith('100'):
                image = pygame.image.load(f'img/Chips/{filename}')
                self.chip_value['100'] = image


