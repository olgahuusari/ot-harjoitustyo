import pygame
import sys
sys.path.append("//wsl.localhost/Ubuntu/home/olgahuusari/ot-harjoitustyo/src/")
from spaceship import SpaceShip

class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((700,500))
        self.clock = pygame.time.Clock()


        self.open_screen()

    
    def open_screen(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        SpaceShip().rotate_r = True
                    if event.key==pygame.K_LEFT:
                        SpaceShip().rotate_l = True
 
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_RIGHT:
                        SpaceShip().rotate_r=False
                    if event.key==pygame.K_LEFT:
                        SpaceShip().rotate_l=False

            if SpaceShip().rotate_r == True:
                SpaceShip().spaceship = pygame.transform.rotate(SpaceShip().spaceship, 10)
            if SpaceShip().rotate_l == True:
                SpaceShip().spaceship = pygame.transform.rotate(SpaceShip().spaceship, -10)

            self.screen.fill((0,0,0))
            self.screen.blit(SpaceShip().spaceship, (SpaceShip().coord()))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game()

