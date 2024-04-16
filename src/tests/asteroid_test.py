import unittest
import pygame
from asteroid import Asteroid

class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid()

    def test_dir_right_d(self):
        self.asteroid.x = 350-(self.asteroid.img.get_width()/2)
        self.asteroid.y = 1000
        self.asteroid.get_degree()
        self.assertEqual(self.asteroid.dir, (0, -2))
    
    def test_dir_right_u(self):
        self.asteroid.x = 350-(self.asteroid.img.get_width()/2)
        self.asteroid.y = -1000
        self.asteroid.get_degree()
        self.assertEqual(self.asteroid.dir, (0, 2))

    def test_dir_right_l(self):
        self.asteroid.x = 1000
        self.asteroid.y = 250-(self.asteroid.img.get_height()/2)
        self.asteroid.get_degree()
        self.assertEqual(self.asteroid.dir, (-2, 0))

    def test_dir_right_r(self):
        self.asteroid.x = -1000
        self.asteroid.y = 250-(self.asteroid.img.get_height()/2)
        self.asteroid.get_degree()
        self.assertEqual(self.asteroid.dir, (2, 0))

    def test_right_degree(self):
        self.asteroid.x = 1000
        self.asteroid.y = 700
        self.assertEqual(round(self.asteroid.get_degree(), 2), 55.33)