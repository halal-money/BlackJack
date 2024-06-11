import pygame.font

from settings import *
from start_button import Button


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("BlackJack")     # title of the game

        self.pygame_icon = pygame.image.load('img/blackjack.png')
        pygame.display.set_icon(self.pygame_icon)   # icon of the game

        # bg of the game
        self.bg_image = pygame.transform.scale(pygame.image.load('img/desk.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.start_button = Button()    # start btn

        # putting header
        self.font = pygame.font.SysFont('bald', 120)  # choosing a font and size
        self.game_header = "BlackJack"   # header text
        self.header_color = (128, 0, 0)  # color of the header
        self.header_surface = self.font.render(self.game_header, True, self.header_color)
        self.header_rect = self.header_surface.get_rect(center=(WINDOW_WIDTH / 2, 340))

    def run(self):
        run = True
        while run:
            self.screen.blit(self.bg_image, (0, 0))     # display bg img
            self.screen.blit(self.header_surface, self.header_rect)
            if self.start_button.run():     # display start btn img
                print('Game Start')
            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()
