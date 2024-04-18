
class Collide:
    def __init__(self):
        self.laser_asteroid = False
        self.asteroid_ship = False

    def laser_hit_asteroid(self, laser, asteroid):
        x = laser.x
        y = laser.y
        if laser.x > 332:
            x = laser.x + laser.img.get_width()
        if laser.y < 236:
            y = laser.y + laser.img.get_height()
        if (asteroid.x < x < asteroid.x+asteroid.img.get_width()) and (
        asteroid.y < y < asteroid.y+asteroid.img.get_height()):
            self.laser_asteroid = True

    def asteroid_hit_ship(self, asteroid, ship):
        if (336 < asteroid.x < 336+ship.img.get_width()) and (
        236 < asteroid.y < 236+ship.img.get_height()):
            self.asteroid_ship = True
