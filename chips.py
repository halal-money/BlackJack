import os

from settings import *

chips_dict: dict = {}
for filename in os.listdir('img/Chips'):
    if filename.startswith('25'):
        image = pygame.image.load(f'img/Chips/{filename}')
        chips_dict['25'] = image
    elif filename.startswith('500'):
        image = pygame.image.load(f'img/Chips/{filename}')
        chips_dict['500'] = image
    elif filename.startswith('50'):
        image = pygame.image.load(f'img/Chips/{filename}')
        chips_dict['50'] = image
    elif filename.startswith('100'):
        image = pygame.image.load(f'img/Chips/{filename}')
        chips_dict['100'] = image

print(chips_dict)


