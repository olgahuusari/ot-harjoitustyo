import unittest
import pygame
from spaceship import SpaceShip
from game import Game
from laser import Laser


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.spaceship = SpaceShip()

    def test_rotate_r_is_false_(self):
        self.assertEqual(self.spaceship.rotate_r, False)

    def test_rotate_l_is_false_(self):
        self.assertEqual(self.spaceship.rotate_l, False)

    def test_laser_correct_degree(self):
        laser = Laser(self.spaceship.degree)
        self.assertEqual(laser.degree, self.spaceship.degree)
    
    def test_laser_move_works(self):
        laser = Laser(0)
        laser.move()
        self.assertEqual((laser.x, laser.y), (360, 250))

    def test_game_no_lasers_at_start(self):
        self.assertEqual(len(self.game.lasers), 0)

