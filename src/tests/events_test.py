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
        self.assertEqual(self.events.rotate_l, True)

    def test_events_rotate_r_works(self):
        event = pygame.event.Event(768, {'unicode': '', 'key': 1073741904, 'mod': 0, 'scancode': 80, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.rotate_r, True)

    def test_events_laser_works(self):
        event = pygame.event.Event(768, {'unicode': ' ', 'key': 32, 'mod': 0, 'scancode': 44, 'window': None})
        self.events.event_handler(event)
        self.assertEqual(self.events.laser, True)