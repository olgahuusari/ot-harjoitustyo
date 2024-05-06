import os
import math
import pygame

dirname = os.path.dirname(__file__)

class Laser:
    """Class that constructs a laser
    """
    def __init__(self, degree):
        """Constructor function

        Args:
            degree (int): degree that states at which direction the laser
            should be pointed at
        """
        super().__init__()
        self.degree = degree
        self.img = self.get_img()
        self.x = 350
        self.y = 250
        self.speed = 1

    def get_img(self):
        """Function that loads the image for the laser and scales it to
        the right size and rotates it at the right angle

        Returns:
            Image: correctly scaled and rotated image of the laser
        """
        img = pygame.image.load(os.path.join(
            dirname, 'assets', 'laser.png'))
        img_ = pygame.transform.scale(img, (20, 2))
        img__ = pygame.transform.rotate(img_, self.degree)
        return img__

    def move(self):
        """Function that moves the laser away from the center
        at the right angle
        """
        self.x += (8+self.speed)*math.cos(math.radians(self.degree))
        self.y -= (8+self.speed)*math.sin(math.radians(self.degree))
        