import os
import math
import pygame

dirname = os.path.dirname(__file__)

class Laser:
    def __init__(self, degree):
        super().__init__()
        self.degree = degree
        self.img = self.get_img()
        self.x = 350
        self.y = 250

    def get_img(self):
        img = pygame.image.load(os.path.join(
            dirname, 'assets', 'laser.png'))
        img_ = pygame.transform.scale(img, (20, 2))
        img__ = pygame.transform.rotate(img_, self.degree)
        return img__

    def move(self):
        self.x += 10*math.cos(math.radians(self.degree))
        self.y -= 10*math.sin(math.radians(self.degree))
        