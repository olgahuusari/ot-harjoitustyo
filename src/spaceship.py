import os
import pygame

dirname = os.path.dirname(__file__)


class SpaceShip:
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load(os.path.join(
            dirname, 'assets', 'spaceship.png'))
        self.rect = self.img.get_rect(center=self.coord())
        self.rotate_r = False
        self.rotate_l = False
        self.degree = 0

    def coord(self):
        center_h = 250-(self.img.get_height()/2)
        center_w = 350-(self.img.get_width()/2)
        return (center_w, center_h)

    def rotate(self):
        spaceship_rot = pygame.transform.rotate(
                self.img, self.degree)
        new_rect = spaceship_rot.get_rect(
                center=self.img.get_rect(center=self.coord()).center)
        return spaceship_rot, new_rect
