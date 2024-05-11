import unittest
from spaceship import SpaceShip

class TestSpaceShip(unittest.TestCase):
    def setUp(self):
        self.spaceship = SpaceShip()

    def setup_is_right(self):
        self.assertEqual(self.spaceship.degree, 0)
        self.assertEqual((self.spaceship.x, self.spaceship.y), (350, 250))
        