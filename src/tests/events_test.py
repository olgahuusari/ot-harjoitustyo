import unittest
import pygame
from events import Events

class TestEvents(unittest.TestCase):
    def setUp(self):
        self.events = Events()

    def test_events_quit_works(self):
        event = pygame.event.Event(256)
        self.events.event_handler(event)
        self.assertEqual(self.events.quit, True)
    
    def test_events_rotate_l_works(self):
        event = pygame.event.Event(768, {'unicode': '', 'key': 1073741903, 'mod': 0, 'scancode': 79, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.rotate, -5)

    def test_events_rotate_r_works(self):
        event = pygame.event.Event(768, {'unicode': '', 'key': 1073741904, 'mod': 0, 'scancode': 80, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.rotate, 5)

    def test_events_laser_works(self):
        event = pygame.event.Event(768, {'unicode': ' ', 'key': 32, 'mod': 0, 'scancode': 44, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.laser, True)

    def test_events_game_over(self):
        event = pygame.event.Event(768, {'unicode': '\r', 'key': 13, 'mod': 0, 'scancode': 40, 'window': None})
        self.events.game_over = True
        self.events.event_handler(event)
        self.assertEqual(self.events.game_over, False)

    def test_events_pause(self):
        event = pygame.event.Event(768, {'unicode': ' ', 'key': 32, 'mod': 0, 'scancode': 44, 'window': None})
        self.events.pause = True
        self.events.event_handler(event)
        self.assertEqual(self.events.pause, False)

    def test_pause_button(self):
        event = pygame.event.Event(1025, {'pos': (659, 13), 'button': 1, 'touch': False, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.button, True)

    def test_pause_pos(self):
        event = pygame.event.Event(1025, {'pos': (659, 13), 'button': 1, 'touch': False, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.event_pos, (659, 13))

    def test_events_rotate_l_stop_works(self):
        event = pygame.event.Event(769, {'unicode': '', 'key': 1073741904, 'mod': 0, 'scancode': 80, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.rotate, 0)

    def test_events_rotate_r_stop_works(self):
        event = pygame.event.Event(769, {'unicode': '', 'key': 1073741903, 'mod': 0, 'scancode': 79, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.rotate, 0)

    