import pygame

class Events:
    def __init__(self):
        self.rotate_l = False
        self.rotate_r = False
        self.quit = False
        self.laser = False

    def event_handler(self, event):
            print(event)
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.rotate_l = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.rotate_r = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.laser = True

            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.rotate_l = False
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.rotate_r = False
