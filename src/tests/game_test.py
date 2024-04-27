import unittest
import pygame
from game import Game
from events import Events
from spaceship import SpaceShip


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_examine_event_module_spaceship_rotate_l(self):
        self.game.spaceship.degree = 0
        self.game.events.rotate_l = True
        self.game.examine_event_module()
        self.assertEqual(self.game.spaceship.degree, -5)

    def test_examine_event_module_spaceship_rotate_r(self):
        self.game.spaceship.degree = 0
        self.game.events.rotate_r = True
        self.game.examine_event_module()
        self.assertEqual(self.game.spaceship.degree, 5)

    def test_laser_added(self):
        lasers = len(self.game.ui.lasers)
        self.game.events.laser = True
        self.game.examine_event_module()
        self.assertEqual(len(self.game.ui.lasers), lasers+1)

    



    
        

