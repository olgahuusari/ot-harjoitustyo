import unittest
import tempfile
import os
from repository import Repository
from save import SaveFile

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.file = tempfile.NamedTemporaryFile(delete=False)
        self.file_path = self.file.name
        self.repository = Repository(self.file_path)

    def test_save(self):
        save_file = SaveFile(15, 2, 2, 45)
        data = self.repository.save(save_file)
        self.assertEqual(data.score, save_file.score)
        self.assertEqual(data.level, save_file.level)
        self.assertEqual(data.ship, save_file.ship)
        self.assertEqual(data.tick, save_file.tick)

    def test_load(self):
        save_file = SaveFile(15, 2, 2, 45)
        self.repository.save(save_file)
        data = self.repository.load()
        self.assertEqual(data.score, save_file.score)
        self.assertEqual(data.level, save_file.level)
        self.assertEqual(data.ship, save_file.ship)
        self.assertEqual(data.tick, save_file.tick)


