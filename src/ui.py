import pygame

class UI:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 500))
        self.lasers = []
        self.asteroids = []
        self.instructions = True
        self.font = pygame.font.SysFont('Arial', 17)

    def draw_window(self, spaceship):
        self.window.fill((0, 0, 0))
        if self.instructions is True:
            text = self.font.render('Rotate the spaceship with left and right arrow keys',
                                    True, (255, 255, 255), (0, 0, 0,))
            self.window.blit(text, (0, 0))
            text2 = self.font.render('Shoot asteroids by pressing the spacebar',
                                     True, (255, 255, 255), (0, 0, 0))
            self.window.blit(text2, (0, 20))

        for asteroid in self.asteroids:
            rect = asteroid.img.get_rect()
            rect = rect.move(asteroid.x, asteroid.y)
            self.window.blit(asteroid.img, rect)
            asteroid.move()

        for laser in self.lasers:
            rect = laser.img.get_rect()
            rect = rect.move(laser.x, laser.y)
            self.window.blit(laser.img, rect)
            laser.move()

        spaceship_rot, new_rect = spaceship.rotate()
        self.window.blit(spaceship_rot, new_rect)
