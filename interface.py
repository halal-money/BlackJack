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

    def run(self):
        run = True
        while run:
            self.screen.blit(self.bg_image, (0, 0))     # display bg img
            if self.start_button.run():     # display start btn img
                print('Game Start')
            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()
