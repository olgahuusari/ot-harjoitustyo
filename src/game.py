import os
import sys
import pygame
from spaceship import SpaceShip
from laser import Laser
from events import Events
from ui import UI
from repository import Repository
from save import SaveFile

dirname = os.path.dirname(__file__)

class Game:
    """Class containing the game loop 
    """
    def __init__(self):
        """Constructor function
        """
        self._clock = pygame.time.Clock()
        self.spaceship = SpaceShip()
        self.events = Events()
        self.ui = UI()
        self.tick = 40
        self.repository = Repository(os.path.join(dirname, "data.csv"))
        self.ui.setup()
        self.load_game()

    def game_loop(self):
        """Function containing the game loop that runs the game
        """

        while True:
            for event in pygame.event.get():
                self.events.event_handler(event)
            self._examine_event_module()

            if self.ui.pause is True:
                self.events.pause = True
                self._pause_loop()

            if self.ui.game_over is True:
                self.events.game_over = True
                self._game_over_loop()
                self.ui.asteroids = self.ui.get_asteroids([], 10 + (self.ui.level-1)*5)

            self.spaceship.img = self.spaceship.get_img(self.ui.choose_ship)

            if self.ui.points >= self.ui.level*10:
                self.ui.level += 1
                self.ui.asteroids = self.ui.get_asteroids(self.ui.asteroids, (self.ui.level-1)*5)
                self.ui.new_ship = True
                self.tick += 5

            self.ui.draw_window(self.spaceship)

            pygame.display.flip()
            self._clock.tick(self.tick)

    def _examine_event_module(self):
        """Function that goes through the the attributes of the 
        Events class and makes appropriate changes to its own attributes
        or those of the UI class
        """
        if self.events.quit is True:
            sys.exit()
        self.spaceship.degree += self.events.rotate
        if self.events.laser is True:
            if len(self.ui.lasers) < 1000:
                laser = Laser(self.spaceship.degree)
                self.ui.lasers.append(laser)
            self.events.laser = False
        if self.events.instructions is False:
            self.ui.instructions = False
        if self.events.pause is True:
            self.ui.pause = True
        if self.events.save is True:
            self.save_game()

        if self.events.button is True:
            self.ui.check_clicks(self.events.event_pos)
            self.events.button = False

    def _game_over_loop(self):
        """Loop that is executed if user loses the game
        """
        while self.events.game_over is True:
            for event in pygame.event.get():
                self.events.event_handler(event)
            if self.events.quit is True:
                sys.exit()
            self.ui.draw_window(self.spaceship)
            pygame.display.flip()
        self.ui.game_over = False
        self.ui.show_ships = False
        self.load_game()

    def _pause_loop(self):
        """Loop that is executed if the game is paused
        """
        while self.events.pause is True:
            for event in pygame.event.get():
                self.events.event_handler(event)
            if self.events.quit is True:
                sys.exit()
            if self.events.button is True:
                self.ui.check_clicks(self.events.event_pos)
                self.events.button = False
            self.spaceship.img = self.spaceship.get_img(self.ui.choose_ship)
            self.ui.draw_window(self.spaceship)
            pygame.display.flip()
        self.ui.pause = False

    def save_game(self):
        file = SaveFile(self.ui.points, self.ui.level, self.ui.choose_ship, self.tick)
        self.repository.save(file)
        self.ui.timer = 10
        return file

    def load_game(self):
        file = self.repository.load()
        self.ui.points = file.score
        self.ui.level = file.level
        self.ui.choose_ship = file.ship
        self.tick = file.tick
