import sys
import pygame
from spaceship import SpaceShip
from laser import Laser
from events import Events
from ui import UI
from level import Level

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.tick = 40
        self.spaceship = SpaceShip()
        self.events = Events()
        self.ui = UI()
        self.level = Level()

    def game_loop(self):

        self.ui.asteroids = self.level.get_asteroids()

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

            if self.ui.game_over is True:
                self.events.game_over = True
                while self.events.game_over is True:
                    for event in pygame.event.get():
                        self.events.event_handler(event)
                    if self.events.quit is True:
                        sys.exit()
                    self.ui.draw_window(self.spaceship)
                    pygame.display.flip()
                self.spaceship = SpaceShip()
                self.events = Events()
                self.ui = UI()
                self.level = Level()
                self.ui.asteroids = self.level.get_asteroids()

            self.ui.draw_window(self.spaceship)
            pygame.display.flip()
            self.clock.tick(self.tick)
