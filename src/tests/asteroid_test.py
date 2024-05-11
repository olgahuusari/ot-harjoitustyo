import unittest
import pygame
from asteroid import Asteroid

class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid()

    def test_dir_right_d(self):
        self.asteroid.x = 350-(self.asteroid.img.get_width()/2)
        self.asteroid.y = 1000
        self.asteroid._get_degree()
        self.assertEqual(self.asteroid.dir, (0, -1))
    
    def test_dir_right_u(self):
        self.asteroid.x = 350-(self.asteroid.img.get_width()/2)
        self.asteroid.y = -1000
        self.asteroid._get_degree()
        self.assertEqual(self.asteroid.dir, (0, 1))

    def test_dir_right_l(self):
        self.asteroid.x = 1000
        self.asteroid.y = 250-(self.asteroid.img.get_height()/2)
        self.asteroid._get_degree()
        self.assertEqual(self.asteroid.dir, (-1, 0))

    def test_dir_right_r(self):
        self.asteroid.x = -1000
        self.asteroid.y = 250-(self.asteroid.img.get_height()/2)
        self.asteroid._get_degree()
        self.assertEqual(self.asteroid.dir, (1, 0))

    def test_right_degree(self):
        self.asteroid.x = 1000
        self.asteroid.y = 700
        self.assertEqual(round(self.asteroid._get_degree(), 2), 55.33)

    def test_move_x(self):
        self.asteroid.y = 240
        self.asteroid.x = 800
        self.asteroid._get_degree()
        self.asteroid.move()
        self.assertEqual(self.asteroid.x, 799)

    def test_move_y(self):
        self.asteroid.y = 800
        self.asteroid.x = 335
        self.asteroid._get_degree()
        self.asteroid.move()
        self.assertEqual(self.asteroid.y, 799)