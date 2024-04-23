import unittest
from collide import Collide
from asteroid import Asteroid
from laser import Laser
from spaceship import SpaceShip

class TestCollide(unittest.TestCase):
    def setUp(self):
        self.collide = Collide()

    def test_laser_hit_asteroid(self):
        asteroid = Asteroid()
        laser = Laser(100)
        asteroid.x, asteroid.y = 0, 0
        laser.x, laser.y = 10, 10
        self.collide.laser_hit_asteroid(laser, asteroid)
        self.assertEqual(self.collide.laser_asteroid, True)

    def test_asteroid_hit_ship(self):
        asteroid = Asteroid()
        ship = SpaceShip()
        asteroid.x, asteroid.y = 336, 236
        self.collide.asteroid_hit_ship(asteroid, ship)
        self.assertEqual(self.collide.asteroid_ship, True)

    def test_laser_hit_asteroid(self):
        asteroid = Asteroid()
        laser = Laser(100)
        asteroid.x, asteroid.y = 0, 0
        laser.x, laser.y = 100, 100
        self.collide.laser_hit_asteroid(laser, asteroid)
        self.assertEqual(self.collide.laser_asteroid, False)

    def test_asteroid_hit_ship(self):
        asteroid = Asteroid()
        ship = SpaceShip()
        asteroid.x, asteroid.y = 100, 100
        self.collide.asteroid_hit_ship(asteroid, ship)
        self.assertEqual(self.collide.asteroid_ship, False)
