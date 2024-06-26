import os
import random
import math
import pygame


dirname = os.path.dirname(__file__)

class Asteroid:
    """Class for generating asteroids, and for moving them.
    """
    def __init__(self):
        """Constructor function, that assigns attributes to one asteroid.
        """
        self.img = self._get_img()
        self.x, self.y = self._get_coord()
        self._degree = self._get_degree()
        self.dir = 0

    def _get_img(self):
        """Function that downloads image for the asteroid
        and scales it to be the right size.

        Returns:
            Img: image for asteroid
        """
        img = pygame.image.load(os.path.join(
            dirname, 'assets', self.get_asteroid()))
        img = pygame.transform.scale(img, (30,20))
        return img

    def get_asteroid(self):
        """Function that randomly chooses which of the images
        is used for this specific asteroid.

        Returns:
            Str: name of a png-file
        """
        number = random.randint(1, 3)
        asteroid = "asteroid" + str(number) + ".png"
        return asteroid

    def _get_coord(self):
        """Function that calculates starting coordinates for the asteroid

        Returns:
            Int: values for x and y coordinates
        """
        x_or_y = random.choice(["x", "y"])
        if x_or_y == "x":
            x = random.randint(-1000, 1700)
            y_side = random.randint(0, 1)
            if y_side == 0:
                y = random.randint(-1000, -self.img.get_height())
            else:
                y = random.randint(500, 1500)
        if x_or_y == "y":
            y = random.randint(-1000, 1500)
            x_side = random.randint(0, 1)
            if x_side == 0:
                x = random.randint(-1000, -self.img.get_width())
            else:
                x = random.randint(700, 1700)
        return x, y

    def _get_degree(self):
        """Function that calculates the degree between a line drawn from
        the center of the screen to the starting coordinates,
        and a line drawn horizontally from the center

        Returns:
            Int: value in degrees
        """
        degree = 0
        center_x = 350-(self.img.get_width()/2)
        center_y = 250-(self.img.get_height()/2)
        if self.x == center_x:
            if self.y > center_y:
                self.dir = (0, -1)
            else:
                self.dir = (0, 1)
        elif self.y == center_y:
            if self.x > center_x:
                self.dir = (-1, 0)
            else:
                self.dir = (1, 0)
        else:
            degree = math.degrees(math.atan(abs(self.x-center_x)/abs(self.y-center_y)))
        return degree

    def move(self):
        """Function that moves the asteroid closer to the center
        using the degree
        """
        if self.dir != 0:
            self.x += self.dir[0]
            self.y += self.dir[1]
        else:
            x_min = 1
            y_min = 1
            if self.x > 350-self.img.get_width()/2:
                x_min = -1
            if self.y > 250-self.img.get_width()/2:
                y_min = -1
            self.x += math.sin(math.radians(self._degree))*x_min
            self.y += math.cos(math.radians(self._degree))*y_min
