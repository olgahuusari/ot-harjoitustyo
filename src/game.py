import sys
import pygame
from spaceship import SpaceShip
from laser import Laser
from events import Events
from asteroid import Asteroid
from ui import UI

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.tick = 40
        self.spaceship = SpaceShip()
        self.events = Events()
        self.ui = UI()

    def game_loop(self):
        for i in range(0, 10):
            asteroid = Asteroid()
            self.ui.asteroids.append(asteroid)

        while True:
            for event in pygame.event.get():
                self.events.event_handler(event)
            if self.events.quit is True:
                sys.exit()
            if self.events.rotate_r is True:
                self.spaceship.degree += 5
            if self.events.rotate_l is True:
                self.spaceship.degree -= 5
            if self.events.laser is True:
                self.ui.lasers.append(Laser(self.spaceship.degree))
                self.events.laser = False
            if self.events.instructions is False:
                self.ui.instructions = False

            self.ui.draw_window(self.spaceship)
            pygame.display.flip()
            self.clock.tick(self.tick)
