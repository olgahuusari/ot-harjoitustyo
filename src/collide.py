
class Collide:
    """Class that calculates if a laser hits an asteroid or an asteroid
    hits the spaceship

    Attributes:
        laser_asteroid (bool) : states whether a laser hit an asteroid or not
        asteroid_ship (bool) : states whether an asteorid hit the ship or not
    """
    def __init__(self):
        """Function that assigns the starting values of the attributes
        """
        self.laser_asteroid = False
        self.asteroid_ship = False

    def laser_hit_asteroid(self, laser, asteroid):
        """Function that calculates whether or not a laser hit has an asteroid

        Args:
            laser (class): class for a specific laser
            asteroid (class): class for a specific asteroid
        """
        if (asteroid.x-laser.img.get_width()+5 <laser.x< asteroid.x+asteroid.img.get_width()-5)and(
        asteroid.y-laser.img.get_height()+5 < laser.y < asteroid.y+asteroid.img.get_height()-5):
            self.laser_asteroid = True

    def asteroid_hit_ship(self, asteroid, ship):
        """Function that calculates whether or not an asteroid hit the spaceship

        Args:
            asteroid (class): class for a specific asteroid
            ship (class): class for the spaceship
        """
        if (ship.x-asteroid.img.get_width() < asteroid.x < ship.x) and (
        ship.y-asteroid.img.get_height() < asteroid.y < ship.y):
            self.asteroid_ship = True
