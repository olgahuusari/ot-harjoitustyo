import os
import random
import math
import pygame


dirname = os.path.dirname(__file__)

class Asteroid:
    def __init__(self):
        self.img = self.get_img()
        self.x, self.y = self.get_coord()
        self.degree = self.get_degree()
        self.dir = 0
        self.get_hit = False
        self.lose_game = False

    def get_img(self):
        img = pygame.image.load(os.path.join(
            dirname, 'assets', self.get_asteroid()))
        img = pygame.transform.scale(img, (30,20))
        return img

    def get_asteroid(self):
        number = random.randint(1, 3)
        asteroid = "asteroid" + str(number) + ".png"
        return asteroid

    def get_coord(self):
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

    def get_degree(self):
        center_x = 350-(self.img.get_width()/2)
        center_y = 250+(self.img.get_height()/2)
        if self.x == center_x:
            if self.y > center_y:
                self.dir = (0, -2)
            else:
                self.dir = (0, 2)
        elif self.y == center_y:
            if self.x > center_x:
                self.dir = (-2, 0)
            else:
                self.dir = (2, 0)
        else:
            degree = math.degrees(math.atan(abs(self.x-center_x)/abs(self.y-center_y)))
        return degree

    def move(self):
        if self.dir != 0:
            self.x += self.dir[0]
            self.y += self.dir[1]
        else:
            x_min = 1
            y_min = 1
            if self.x > 350:
                x_min = -1
            if self.y > 250:
                y_min = -1
            self.x += 1*math.sin(math.radians(self.degree))*x_min
            self.y += 1*math.cos(math.radians(self.degree))*y_min
