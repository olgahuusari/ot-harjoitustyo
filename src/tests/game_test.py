import unittest
from spaceship import SpaceShip


class TestSpaceShip(unittest.TestCase):
    def setUp(self):
        self.spaceship = SpaceShip()

    def test_rotate_r_is_false_(self):
        self.assertEqual(self.spaceship.rotate_r, False)

    def test_rotate_l_is_false_(self):
        self.assertEqual(self.spaceship.rotate_l, False)
