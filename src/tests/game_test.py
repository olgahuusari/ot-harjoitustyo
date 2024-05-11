import unittest
import pygame
from game import Game
from events import Events
from spaceship import SpaceShip
from laser import Laser


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_examine_event_module_spaceship_rotate_l(self):
        self.game.spaceship.degree = 0
        self.game.events.rotate = -5
        self.game._examine_event_module()
        self.assertEqual(self.game.spaceship.degree, -5)

    def test_examine_event_module_spaceship_rotate_r(self):
        self.game.spaceship.degree = 0
        self.game.events.rotate = 5
        self.game._examine_event_module()
        self.assertEqual(self.game.spaceship.degree, 5)

    def test_laser_added(self):
        lasers = len(self.game.ui.lasers)
        self.game.events.laser = True
        self.game._examine_event_module()
        self.assertEqual(len(self.game.ui.lasers), lasers+1)

    def test_laser_not_added(self):
        for _ in range(1000):
            self.game.ui.lasers.append(Laser(0))
        lasers = len(self.game.ui.lasers)
        self.game.events.laser = True
        self.game._examine_event_module()
        self.assertEqual(len(self.game.ui.lasers), lasers)

    def test_instructions(self):
        self.game.events.instructions = False
        self.game._examine_event_module()
        self.assertEqual(self.game.ui.instructions, False)

    def test_pause(self):
        self.game.events.pause = True
        self.game._examine_event_module()
        self.assertEqual(self.game.ui.pause, True)

    def test_button(self):
        self.game.events.button = True
        self.game._examine_event_module()
        self.assertEqual(self.game.events.button, False)

    



    
        

