import pygame
import os

dirname = os.path.dirname(__file__)

class SpaceShip:
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(os.path.join(dirname, 'assets', 'spaceship.png'))
        self.rect = self.img.get_rect(center = self.coord())
        self.rotate_r = False
        self.rotate_l = False
        self.degree = 0

    def coord(self):
        return((350-(self.img.get_width()/2), 250-(self.img.get_height()/2)))
    