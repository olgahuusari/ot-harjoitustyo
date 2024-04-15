import unittest
from laser import Laser

class TestLaser(unittest.TestCase):
    def setUp(self):
        self.laser = Laser()

    def test_laser_move_works(self):
        laser = Laser(0)
        laser.move()
        self.assertEqual((laser.x, laser.y), (360, 250))

    def test_laser_correct_degree(self):
        laser = Laser(self.spaceship.degree)
        self.assertEqual(laser.degree, self.spaceship.degree)