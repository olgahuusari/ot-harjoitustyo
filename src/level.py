from asteroid import Asteroid

class Level:
    def __init__(self):
        self.level = 1

    def get_asteroids(self):
        asteroids = []
        for i in range(0, 10):
            asteroid = Asteroid()
            asteroids.append(asteroid)
        return asteroids
