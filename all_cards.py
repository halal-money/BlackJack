import os
import pygame

ace = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []
jack = []
queen = []
king = []

for filename in os.listdir('img/all_cards'):
    if filename.startswith('ace_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        ace.append(image)
    elif filename.startswith('02_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        two.append(image)
    elif filename.startswith('03_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        three.append(image)
    elif filename.startswith('04_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        four.append(image)
    elif filename.startswith('05_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        five.append(image)
    elif filename.startswith('06_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        six.append(image)
    elif filename.startswith('07_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        seven.append(image)
    elif filename.startswith('08_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        eight.append(image)
    elif filename.startswith('09_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        nine.append(image)
    elif filename.startswith('10_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        ten.append(image)
    elif filename.startswith('jack_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        jack.append(image)
    elif filename.startswith('queen_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        queen.append(image)
    elif filename.startswith('king_of_'):
        image = pygame.image.load(f"img/all_cards/{filename}")
        king.append(image)
all_cards = [
    {'ace': ace},
    {'two': two},
    {'three': three},
    {'four': four},
    {'five': five},
    {'six': six},
    {'seven': seven},
    {'eight': eight},
    {'nine': nine},
    {'ten': ten},
    {'jack': jack},
    {'queen': queen},
    {'king': king}
]
print(all_cards)