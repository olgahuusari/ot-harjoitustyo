
class Collide:
    def __init__(self):
        self.laser_asteroid = False
        self.asteroid_ship = False

    def laser_hit_asteroid(self, laser, asteroid):
        if (asteroid.x-laser.img.get_width() < laser.x < asteroid.x+asteroid.img.get_width()) and (
        asteroid.y-laser.img.get_height() < laser.y < asteroid.y+asteroid.img.get_height()):
            self.laser_asteroid = True

    def asteroid_hit_ship(self, asteroid, ship):
        if (ship.x-asteroid.img.get_width() < asteroid.x < ship.x+ship.img.get_width()-15) and (
        ship.y-asteroid.img.get_height() < asteroid.y < ship.y+ship.img.get_height()-15):
            self.asteroid_ship = True
