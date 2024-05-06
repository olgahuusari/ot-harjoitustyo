import os
import pygame

dirname = os.path.dirname(__file__)


class SpaceShip:
    """Class for the spaceship
    """
    def __init__(self):
        """Constructor function that assigns the starting values of the
        attributes
        """
        super().__init__()
        self.img = pygame.image.load(os.path.join(
            dirname, 'assets', 'spaceship1.png'))
        self.rect = self.img.get_rect(center=(350, 250))
        self.degree = 0
        self.x, self.y = 350, 250
        self.speed = 1

    def get_img(self, number):
        """Functions that loads the correct image of the spaceship

        Args:
            number (int): number that shows which picture to load

        Returns:
            Image: image of the spaceship the user has picked
        """
        return pygame.image.load(os.path.join(
            dirname, 'assets', 'spaceship' + str(number) + '.png'))

    def rotate(self):
        """Function that generates a rotated picture of the spaceship
        and creates a rectangle of it

        Returns:
            Img, rect : image and rectangle of the rotated spaceship
        """
        spaceship_rot = pygame.transform.rotate(
                self.img, (self.degree+self.speed))
        new_rect = spaceship_rot.get_rect(
                center=self.img.get_rect(center=(350, 250)).center)
        return spaceship_rot, new_rect
