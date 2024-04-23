import unittest
from level import Level

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level()

    def test_asteroid_list(self):
        self.assertEqual(len(self.level.get_asteroids()), 10)