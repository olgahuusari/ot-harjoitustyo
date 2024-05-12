import pathlib
from save import SaveFile

class Repository:
    """class for saving and loading gaming data
    """
    def __init__(self, file_path):
        """constructor function

        Args:
            file_path (str): path to the .cvs file
        """
        self._file_path = file_path
        self.loaded_file = SaveFile(0, 1, 1, 40)

    def save(self, save_file):
        """function that saves current gaming data

        Args:
            save_file (SaveFile object): SaveFile object containing current data of
            the situation in the game

        Returns:
            SaveFile object: same as the one as the attribute
        """
        self._ensure_file_exists()
        self._write(save_file)
        return save_file

    def load(self):
        """function that loads the data that has been saved

        Returns:
            SaveFile object: from the _read function
        """
        self._ensure_file_exists()
        return self._read()

    def _ensure_file_exists(self):
        """checks if the file path exists. If not, a file is created
        """
        if pathlib.Path(self._file_path).exists():
            return
        pathlib.Path(self._file_path).touch()

        with open(self._file_path, "w", encoding="utf-8") as file:
            data = "0;1;1;40"
            file.write(data)

    def _read(self):
        """Reads the data from the cvs file

        Returns:
            SaveFile object: containing previously saved data
        """
        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                self._split_save_file(row)
        return self.loaded_file

    def _write(self, file):
        """Creates a string containing current data from the game and writes it to the cvs file

        Args:
            file (SaveFile object): containing current data from the game
        """
        with open(self._file_path, "w", encoding="utf-8") as f:
            score = str(file.score)
            level = str(file.level)
            ship = str(file.ship)
            tick = str(file.tick)

            data = score + ";" + level + ";" + ship + ";" + tick

            f.write(data)

    def _split_save_file(self, file):
        """Splits a string to a list

        Args:
            file (str): string that is in the cvs file
        """
        parts = file.split(";")
        self.loaded_file.score = int(parts[0])
        self.loaded_file.level = int(parts[1])
        self.loaded_file.ship = int(parts[2])
        self.loaded_file.tick = int(parts[3])
