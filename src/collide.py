
class Collide:
    def __init__(self):
        self.laser_asteroid = False
        self.asteroid_ship = False

    def laser_hit_asteroid(self, laser, asteroid):
        if (asteroid.x-laser.img.get_width()+5 <laser.x< asteroid.x+asteroid.img.get_width()-5)and(
        asteroid.y-laser.img.get_height()+5 < laser.y < asteroid.y+asteroid.img.get_height()-5):
            self.laser_asteroid = True

    def asteroid_hit_ship(self, asteroid, ship):
        if (ship.x-asteroid.img.get_width() < asteroid.x < ship.x) and (
        ship.y-asteroid.img.get_height() < asteroid.y < ship.y):
            self.asteroid_ship = True
