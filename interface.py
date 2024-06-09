from settings import *


class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("BlackJack")
        self.pygame_icon = pygame.image.load('img/blackjack.png')
        pygame.display.set_icon(self.pygame_icon)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()
