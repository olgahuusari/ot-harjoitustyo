import pygame
from collide import Collide
from asteroid import Asteroid

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

    def draw_window(self, spaceship):
        self.window.fill((0, 0, 0))
        points = self.font.render(f'Points: {self.points}', True, (255, 255, 255), (0, 0, 0))
        self.window.blit(points, (600, 0))

        if self.instructions is True:
            text = self.font.render('Rotate the spaceship with left and right arrow keys',
                                    True, (255, 255, 255), (0, 0, 0,))
            self.window.blit(text, (0, 0))
            text2 = self.font.render('Shoot asteroids by pressing the spacebar',
                                     True, (255, 255, 255), (0, 0, 0))
            self.window.blit(text2, (0, 20))

        for asteroid in self.asteroids:
            self.collide.asteroid_hit_ship(asteroid, spaceship)
            if self.collide.asteroid_ship is True:
                self.game_over = True
            rect = asteroid.img.get_rect()
            rect = rect.move(asteroid.x, asteroid.y)
            self.window.blit(asteroid.img, rect)
            asteroid.move()

        for laser in self.lasers:
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
