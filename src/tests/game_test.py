import unittest
import pygame
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_no_lasers_at_start(self):
        self.assertEqual(len(self.game.lasers), 0)

    
        

