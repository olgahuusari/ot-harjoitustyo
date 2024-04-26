import pygame
from collide import Collide
from asteroid import Asteroid
from spaceship import SpaceShip

class UI:
    def __init__(self):
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
        self.ship_rect = self.ship_text.get_rect(topleft=(650, 80))
        self.choose_ship = 1

    def draw_window(self, spaceship):
        self.window.fill((0, 0, 0))
        points = self.font.render(f'Points: {self.points}', True, (255, 255, 255), (0, 0, 0))
        self.window.blit(points, (550, 0))
        level = self.font.render(f'Level: {self.level}', True, (255, 255, 255), (0, 0, 0))
        self.window.blit(level, (640, 0))

        if self.game_over is True:
            game_lost = self.font.render('Game Over. Start a new one by pressing space!',
                                          True, (255, 255, 255), (0, 0, 0))
            self.window.blit(game_lost, (200, 150))

        if self.level >= 2:
            self.window.blit(self.ship_text, (650, 80))

        if self.show_ships is True:
            self.ship_selection()

        if self.instructions is True:
            text = self.font.render('Rotate the spaceship with left and right arrow keys',
                                    True, (255, 255, 255), (0, 0, 0,))
            self.window.blit(text, (0, 0))
            text2 = self.font.render('Shoot asteroids by pressing the spacebar',
                                     True, (255, 255, 255), (0, 0, 0))
            self.window.blit(text2, (0, 20))

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
            laser.move()

        spaceship_rot, new_rect = spaceship.rotate()
        self.window.blit(spaceship_rot, new_rect)

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
            asteroid.move()

    def get_asteroids(self, asteroids, i):
        for n in range(0, i):
            asteroid = Asteroid()
            asteroids.append(asteroid)
        return asteroids

    def check_clicks(self, event_pos):
        if self.ship_rect.collidepoint(event_pos) is True:
            if self.show_ships is True:
                self.show_ships = False
                return
            self.show_ships = True
        for ship in self.ships:
            if ship[1].collidepoint(event_pos):
                index = self.ships.index(ship)
                if index == 0:
                    self.choose_ship = 1
                else:
                    self.choose_ship = index*2

    def get_ships(self):
        ship = SpaceShip()
        list = [1, 2, 4, 6, 8]
        for i in list:
            ship_img = ship.get_img(i)
            ship_pos = (640, 110+list.index(i)*50)
            ship_rect = ship_img.get_rect(topleft=ship_pos)
            self.ships.append((ship_img, ship_rect, ship_pos))

    def ship_selection(self):
        for ship in self.ships:
            if self.ships.index(ship) < self.level:
                self.window.blit(ship[0], ship[2])
