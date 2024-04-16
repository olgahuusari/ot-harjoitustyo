import unittest
import pygame
from asteroid import Asteroid

class TestAsteroid(unittest.TestCase):
    def setUp(self):
        self.asteroid = Asteroid()