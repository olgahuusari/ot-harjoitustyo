import sys
import pygame
from spaceship import SpaceShip
from laser import Laser
from events import Events


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 500))
        self.clock = pygame.time.Clock()
        self.spaceship = SpaceShip()
        self.events = Events()
        self.lasers = []
        self.tick = 40

    def open_window(self):

        while True:
            for event in pygame.event.get():
                self.events.event_handler(event)
            if self.events.quit == True:
                sys.exit()
            if self.events.rotate_r == True:
                self.spaceship.degree += 5
            if self.events.rotate_l == True:
                self.spaceship.degree -= 5
            if self.events.laser == True:
                self.lasers.append(Laser(self.spaceship.degree))
                self.events.laser = False

            self.window.fill((0, 0, 0))

            for laser in self.lasers:
                rect = laser.img.get_rect()
                rect = rect.move(laser.x, laser.y)
                self.window.blit(laser.img, rect)
                laser.move()

            spaceship_rot, new_rect = self.spaceship.rotate()
            self.window.blit(spaceship_rot, new_rect)

            pygame.display.flip()
            self.clock.tick(self.tick)


