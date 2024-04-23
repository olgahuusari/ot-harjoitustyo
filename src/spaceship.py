import os
import pygame

dirname = os.path.dirname(__file__)


class SpaceShip:
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(os.path.join(
            dirname, 'assets', 'spaceship.png'))
        self.rect = self.img.get_rect(center=(336, 236))
        self.degree = 0
        self.x, self.y = 336, 236

    def rotate(self):
        spaceship_rot = pygame.transform.rotate(
                self.img, self.degree)
        new_rect = spaceship_rot.get_rect(
                center=self.img.get_rect(center=(336, 236)).center)
        return spaceship_rot, new_rect
