import pygame

class Events:
    """Class that handles pygame events
    """
    def __init__(self):
        """Constructor function
        """
        self.rotate = 0
        self.quit = False
        self.laser = False
        self.instructions = True
        self.game_over = False
        self.pause = False
        self.button = False
        self.event_pos = (0, 0)
        self.save = False

    def event_handler(self, event):
        """Function that evaluates a single event and changes the class'
        attributes accordingly

        Args:
            event (pygame event)
        """
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            self._key_down_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.button = True
            self.event_pos = event.pos

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                self.rotate = 0

    def _key_down_events(self, event):
        """Handles events that occur when a key is pressed

        Args:
            event (pygame event)
        """
        if event.key == pygame.K_RIGHT:
            self.rotate = -5
        if event.key == pygame.K_LEFT:
            self.rotate = 5
        if event.key == pygame.K_SPACE:
            if self.pause is True:
                self.pause = False
                return
            self.laser = True
            self.instructions = False
        if event.key == pygame.K_p:
            self.pause = True
        if event.key == pygame.K_s:
            self.save = True
        if event.key == pygame.K_RETURN:
            if self.game_over is True:
                self.game_over = False
