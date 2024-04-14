import os
import pygame

dirname = os.path.dirname(__file__)


class SpaceShip:
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(os.path.join(
            dirname, 'assets', 'spaceship.png'))
        self.rect = self.img.get_rect(center=(350, 250))
        self.rotate_r = False
        self.rotate_l = False
        self.degree = 0

    def rotate(self):
        spaceship_rot = pygame.transform.rotate(
                self.img, self.degree)
        new_rect = spaceship_rot.get_rect(
                center=self.img.get_rect(center=(350, 250)).center)
        return spaceship_rot, new_rect
