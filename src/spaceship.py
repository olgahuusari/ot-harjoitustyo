import pygame
import os

dirname = os.path.dirname(__file__)

class SpaceShip:
    def __init__(self):
        super().__init__()
        self.spaceship = pygame.image.load(os.path.join(dirname, 'assets', 'spaceship.png'))
        self.rotate_r = False
        self.rotate_l = False

    def coord(self):
        return((350-(self.spaceship.get_width()/2), 250-(self.spaceship.get_height()/2)))