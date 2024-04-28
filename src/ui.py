import pygame
from collide import Collide
from asteroid import Asteroid
from spaceship import SpaceShip

class UI:
    """Class that handles user interface
    """
    def __init__(self):
        """Constructor function that assigns the starting values of the
        attributes
        """
        pygame.init()
        self.collide = Collide()
        self.window = pygame.display.set_mode((700, 500))
        self.lasers = []
        self.asteroids = []
        self.instructions = True
        self.font = pygame.font.SysFont('Arial', 17)
        self.game_over = False
        self.points = 0
        self.level = 1
        self.ships = []
        self.show_ships = False
        self.ship_text = self.font.render('Ships', True, (0, 0, 0), (255, 255, 255))
        self.ship_rect = pygame.Rect(630, 80, 100, 20)
        self.pause_text = self.font.render('Pause game', True, (0, 0, 0), (255, 255, 255))
        self.pause_rect = pygame.Rect(610, 0, 90, 20)
        self.pause = False
        self.choose_ship = 1
        self.new_ship = False

    def setup(self):
        """Function that is executed at the start of the game that creates
        lists of asteroids and spaceship options
        """
        self.asteroids = self.get_asteroids([], 10)
        self.get_ships()

    def draw_window(self, spaceship):
        """Function that creates the game window

        Args:
            spaceship (class): class for the spaceship
        """
        self.window.fill((0, 0, 0))
        points = self.font.render(f'Points: {self.points}', True, (255, 255, 255), (0, 0, 0))
        self.window.blit(points, (360, 0))
        level = self.font.render(f'Level: {self.level}', True, (255, 255, 255), (0, 0, 0))
        self.window.blit(level, (280, 0))
        pygame.draw.rect(self.window, (255, 255, 255), (610, 0, 90, 20))
        self.window.blit(self.pause_text, (610, 0))

        self.examine_attributes()

        pygame.draw.rect(self.window, (255, 255, 255), (630, 80, 100, 20))
        self.window.blit(self.ship_text, (630, 80))

        self.examine_lasers()

        spaceship_rot, new_rect = spaceship.rotate()
        self.window.blit(spaceship_rot, new_rect)

        self.examine_asteroids(spaceship)

    def get_asteroids(self, asteroids, i):
        """Function that either creates a list of the asteorids or adds
        new ones

        Args:
            asteroids (list): empty or non-empty list of asteroids
            i (int): number of asteroids that are added to the list

        Returns:
            list: list of asteroids that are shown in the game
        """
        for _ in range(0, i):
            asteroid = Asteroid()
            asteroids.append(asteroid)
        return asteroids

    def examine_attributes(self):
        """Function that examines the attributes and shows the correct
        things on the screen
        """
        if self.game_over is True:
            game_lost = self.font.render('Game Over. Start a new one by pressing space!',
                                          True, (255, 255, 255), (0, 0, 0))
            self.window.blit(game_lost, (200, 150))

        if self.pause is True:
            pause = self.font.render('Game paused. Continue by pressing space.',
                                     True, (255, 255, 255), (0, 0, 0))
            self.window.blit(pause, (200, 180))

        if self.new_ship is True:
            new_ship = self.font.render('New ship!!', True, (255, 255, 255), (0, 0, 0))
            self.window.blit(new_ship, (630, 100))

        if self.show_ships is True:
            self.ship_selection()

        if self.instructions is True:
            text = self.font.render('Rotate the spaceship with left and right arrow keys',
                                    True, (255, 255, 255), (0, 0, 0,))
            self.window.blit(text, (200, 130))
            text2 = self.font.render('Shoot asteroids by pressing the spacebar',
                                     True, (255, 255, 255), (0, 0, 0))
            self.window.blit(text2, (200, 150))

    def examine_lasers(self):
        """Function that goes through lasers that are shown on screen
        and calls the collide module to check whether they have hit asteroids
        or gone off the screen
        After that the function calls the laser module to move the lasers
        """
        for laser in self.lasers:
            if self.game_over is True:
                continue
            for asteroid in self.asteroids:
                self.collide.laser_hit_asteroid(laser, asteroid)
                if self.collide.laser_asteroid is True:
                    self.points += 1
                    self.collide.laser_asteroid = False
                    self.asteroids.remove(asteroid)
                    new_asteroid = Asteroid()
                    self.asteroids.append(new_asteroid)
                    self.lasers.remove(laser)
            if (laser.x < -laser.img.get_width() or laser.x > 700) or (
            laser.y < -laser.img.get_height() or laser.y > 500):
                self.lasers.remove(laser)
            rect = laser.img.get_rect()
            rect = rect.move(laser.x, laser.y)
            self.window.blit(laser.img, rect)
            if self.pause is True:
                continue
            laser.move()

    def examine_asteroids(self, spaceship):
        """Function that goes through asteroids shown on screen and calls
        for the collide module to calculate whether they have hit the ship.
        After that the function calls for the asteroid module to move them

        Args:
            spaceship (class): class for the spaceship
        """
        for asteroid in self.asteroids:
            if self.game_over is True:
                continue
            self.collide.asteroid_hit_ship(asteroid, spaceship)
            if self.collide.asteroid_ship is True:
                self.game_over = True
                self.collide.asteroid_ship = False
                continue
            rect = asteroid.img.get_rect()
            rect = rect.move(asteroid.x, asteroid.y)
            self.window.blit(asteroid.img, rect)
            if self.pause is True:
                continue
            asteroid.move()

    def check_clicks(self, event_pos):
        """Function that is called when the user has pressed a button on
        screen. It calculates which button was pressed and changes the 
        attributes accordingly

        Args:
            event_pos ((int, int)): coordinates of where the user clicked
        """
        if self.pause_rect.collidepoint(event_pos) is True:
            self.pause = True
        if self.ship_rect.collidepoint(event_pos) is True:
            self.new_ship = False
            if self.show_ships is True:
                self.show_ships = False
                return
            self.show_ships = True
        if self.show_ships is True:
            for ship in self.ships:
                if ship[1].collidepoint(event_pos) and self.ships.index(ship) < self.level:
                    self.choose_ship = self.ships.index(ship)+1

    def get_ships(self):
        """Function that loads the image, creates rectangle and calculates the position
        of the different ship options. These are added to the attribute ships
        """
        ship = SpaceShip()
        for i in range(1, 6):
            ship_img = ship.get_img(i)
            ship_pos = (650, 70+i*50)
            ship_rect = ship_img.get_rect(topleft=ship_pos)
            self.ships.append((ship_img, ship_rect, ship_pos))

    def ship_selection(self):
        """Functions that shows the different ship options on screen
        """
        for ship in self.ships:
            if self.ships.index(ship) < self.level:
                self.window.blit(ship[0], ship[2])
