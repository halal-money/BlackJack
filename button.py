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


class ExitButton(Button):
    def __init__(self):
        button = pygame.image.load('img/exit.png')
        super().__init__(button=button, btn_size=(50, 50), btn_rect=(1150, 60))
