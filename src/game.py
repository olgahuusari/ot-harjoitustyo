import pygame
from spaceship import SpaceShip

class Game:
    def __init__(self):
        pygame.init()
        self.window=pygame.display.set_mode((700,500))
        self.clock = pygame.time.Clock()
        self.spaceship = SpaceShip()
        self.tick = 40


        self.open_window()

    
    def open_window(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        self.spaceship.rotate_l = True
                    if event.key==pygame.K_LEFT:
                        self.spaceship.rotate_r = True
 
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        self.spaceship.rotate_l=False
                    if event.key==pygame.K_LEFT:
                        self.spaceship.rotate_r=False

            if self.spaceship.rotate_r == True:
                self.spaceship.degree += 10
            if self.spaceship.rotate_l == True:
                self.spaceship.degree -= 10
            spaceship_rot = pygame.transform.rotate(self.spaceship.img, self.spaceship.degree)
            new_rect = spaceship_rot.get_rect(center = self.spaceship.img.get_rect(center = (self.spaceship.coord())).center)

            self.window.fill((0,0,0))
            self.window.blit(spaceship_rot, new_rect)
            pygame.display.flip()
            self.clock.tick(self.tick)


if __name__ == "__main__":
    Game()

