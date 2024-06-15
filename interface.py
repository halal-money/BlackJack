import pygame.font
import time

from settings import *
from button import Button, ExitButton
from alert import Alert
from display_chips import Chips


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("BlackJack")     # title of the game

        self.game_icon = pygame.image.load('img/blackjack.png')
        pygame.display.set_icon(self.game_icon)   # icon of the game

        # bg of the game
        self.bg_image = pygame.transform.scale(pygame.image.load('img/desk.jpg'), (WINDOW_WIDTH, WINDOW_HEIGHT))

        start_button = pygame.image.load('img/start_button.png')
        self.start_button = Button(button=start_button, btn_size=(250, 200), btn_rect=(320, 670))    # start btn

        quit_button = pygame.image.load('img/quit.png')
        self.quit_button = Button(button=quit_button, btn_size=(250, 200), btn_rect=(620, 670))    # quit btn

        self.exit_button = ExitButton()  # exit button

        # putting header
        self.font = pygame.font.SysFont('bald', 120)  # choosing a font and size
        self.game_header = "BlackJack"   # header text
        self.header_color = (128, 0, 0)  # color of the header
        self.header_surface = self.font.render(self.game_header, True, self.header_color)
        self.header_rect = self.header_surface.get_rect(center=(WINDOW_WIDTH / 2, 215))

        # center the game icon
        self.icon_size = pygame.transform.scale(self.game_icon, (200, 150))
        self.icon_rect = self.icon_size.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # alert
        self.alert = Alert()
        self.alert_start_time = None  # track when the alert starts
        self.show_elements = True

        # chips
        self.chips = Chips()

    def run(self):
        run = True
        while run:
            self.screen.blit(self.bg_image, (0, 0))  # display bg img

            if self.exit_button.run():    # If ExitButton gets clicked
                run = False    # Close window

            if self.show_elements:
                self.screen.blit(self.header_surface, self.header_rect)  # display header
                self.screen.blit(self.icon_size, self.icon_rect)    # display game icon
                if self.start_button.run():     # display start btn img
                    print('Game Start')
                    self.alert_start_time = time.time()

                if self.quit_button.run():
                    print('Game Over')
                    run = False

            # Display alert if within 3 seconds of clicking the button
            if self.alert_start_time:
                if time.time() - self.alert_start_time < 3:
                    self.alert.run()
                else:
                    self.alert_start_time = None
                    self.show_elements = False

            if not self.show_elements:
                self.chips.run()

            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()
