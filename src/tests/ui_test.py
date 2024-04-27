import unittest
from ui import UI
from spaceship import SpaceShip

class TestUI(unittest.TestCase):
    def setUp(self):
        self.ui = UI()

    def test_setup_asteroids(self):
        self.ui.setup()
        self.assertEqual(len(self.ui.asteroids), 10)

    def test_setup_ships(self):
        self.ui.setup()
        self.assertEqual(len(self.ui.ships), 5)

    def test_check_clicks_pause(self):
        event_pos = (694, 13)
        self.ui.check_clicks(event_pos)
        self.assertEqual(self.ui.pause, True)

    def test_check_clicks_ship_menu(self):
        event_pos = (635, 85)
        self.ui.check_clicks(event_pos)
        self.assertEqual(self.ui.show_ships, True)
    
    def test_check_clicks_new_ships(self):
        event_pos = (635, 85)
        self.ui.new_ship = True
        self.ui.check_clicks(event_pos)
        self.assertEqual(self.ui.new_ship, False)

    def test_check_clicks_close_ship_menu(self):
        event_pos = (635, 85)
        self.ui.show_ships = True
        self.ui.check_clicks(event_pos)
        self.assertEqual(self.ui.show_ships, False)

    def test_examine_asteroids_game_over(self):
        spaceship = SpaceShip()
        self.ui.setup()
        asteroids = self.ui.asteroids
        self.game_over = True
        self.ui.examine_asteroids(spaceship)
        self.assertEqual(asteroids, self.ui.asteroids)

    def test_examine_asteroids_pause(self):
        spaceship = SpaceShip()
        self.ui.setup()
        asteroids = self.ui.asteroids
        self.pause = True
        self.ui.examine_asteroids(spaceship)
        self.assertEqual(asteroids, self.ui.asteroids)

