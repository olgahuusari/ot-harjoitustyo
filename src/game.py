import sys
import pygame
from spaceship import SpaceShip
from laser import Laser
from events import Events
from ui import UI

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.spaceship = SpaceShip()
        self.events = Events()
        self.ui = UI()
        self.tick = 40

    def game_loop(self):

        self.ui.asteroids = self.ui.get_asteroids([], 10)
        self.ui.get_ships()

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

            if self.events.button is True:
                self.ui.check_clicks(self.events.event_pos)
                self.events.button = False
            self.spaceship.img = self.spaceship.get_img(self.ui.choose_ship)

            if self.ui.game_over is True:
                self.events.game_over = True
                self.game_over_loop()
                self.ui.asteroids = self.ui.get_asteroids([], 10 + (self.ui.level-1)*5)

            self.ui.draw_window(self.spaceship)
            if self.ui.points >= self.ui.level*10:
                self.ui.level += 1
                self.ui.asteroids = self.ui.get_asteroids(self.ui.asteroids, (self.ui.level-1)*5)
                self.tick += 5

            pygame.display.flip()
            self.clock.tick(self.tick)

    def game_over_loop(self):
        while self.events.game_over is True:
            for event in pygame.event.get():
                self.events.event_handler(event)
            if self.events.quit is True:
                sys.exit()
            self.ui.draw_window(self.spaceship)
            pygame.display.flip()
        self.ui.game_over = False
        self.ui.level = 1
        self.ui.points = 0
