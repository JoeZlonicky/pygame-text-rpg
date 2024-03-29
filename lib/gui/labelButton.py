import pygame
from lib.gui.button import Button


class LabelButton(Button):
    def __init__(self, text, func, *funcArgs, fontSize=24, x=0, y=0):
        self.text = text
        self.font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf",
                                     fontSize)
        image = self.font.render(self.text, True, (200, 200, 200))
        super().__init__(image, func, *funcArgs, x=x, y=y)

    def hover(self):
        super().hover()
        self.image = self.font.render(">" + self.text, True, (255, 255, 255))

    def unhover(self):
        super().unhover()
        self.image = self.font.render(self.text, True, (200, 200, 200))
