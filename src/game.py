import sys
import pygame
from spaceship import SpaceShip
from laser import Laser


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((700, 500))
        self.clock = pygame.time.Clock()
        self.spaceship = SpaceShip()
        self.lasers = []
        self.tick = 40

        self.open_window()

    def open_window(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.spaceship.rotate_l = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.spaceship.rotate_r = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    new_laser = Laser(self.spaceship.degree)
                    self.lasers.append(new_laser)

                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    self.spaceship.rotate_l = False
                if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    self.spaceship.rotate_r = False

            if self.spaceship.rotate_r is True:
                self.spaceship.degree += 10
            if self.spaceship.rotate_l is True:
                self.spaceship.degree -= 10

            self.window.fill((0, 0, 0))

            for laser in self.lasers:
                rect = laser.img.get_rect()
                rect = rect.move(laser.x, laser.y)
                self.window.blit(laser.img, rect)
                laser.move()

            spaceship_rot, new_rect = self.spaceship.rotate()
            self.window.blit(spaceship_rot, new_rect)

            pygame.display.flip()
            self.clock.tick(self.tick)


if __name__ == "__main__":
    Game()
