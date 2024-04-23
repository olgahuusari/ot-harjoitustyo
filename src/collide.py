
class Collide:
    def __init__(self):
        self.laser_asteroid = False
        self.asteroid_ship = False

    def laser_hit_asteroid(self, laser, asteroid):
        if (asteroid.x-laser.img.get_width() < laser.x < asteroid.x+asteroid.img.get_width()) and (
        asteroid.y-laser.img.get_height() < laser.y < asteroid.y+asteroid.img.get_height()):
            self.laser_asteroid = True
            print(laser.x, laser.y, laser.img.get_width(), laser.img.get_height(), asteroid.x, asteroid.y, asteroid.img.get_width(), asteroid.img.get_height())

    def asteroid_hit_ship(self, asteroid, ship):
        if (ship.x-asteroid.img.get_width() < asteroid.x < ship.x) and (
        ship.y-asteroid.img.get_height() < asteroid.y < ship.y):
            self.asteroid_ship = True
