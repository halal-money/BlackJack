from settings import *


class Button:
    def __init__(self, button, btn_size, btn_rect):
        self.button = button     # start_btn img
        self.button_size = pygame.transform.scale(self.button, btn_size)  # changed the size of the start btn
        self.rect = self.button_size.get_rect(bottomleft=btn_rect)
        self.surface = pygame.display.get_surface()
        self.clicked = False

    def run(self):
        action = False
        pos = pygame.mouse.get_pos()    # getting mouse position

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.surface.blit(self.button_size, self.rect)
        return action
class exitButton(Button): #exitButton class inherits from Button
    def __init__(self):
        super().__init__()
        self.button = pygame.image.load('exit.png')
        self.button_size = pygame.transform.scale(self.button, (50, 50))
        self.rect = self.button_size.get_rect(topright=(1200, 00))
        self.surface = pygame.display.get_surface()
        self.clicked = False

    def exit_run(self):

        super(exitButton, self).run()