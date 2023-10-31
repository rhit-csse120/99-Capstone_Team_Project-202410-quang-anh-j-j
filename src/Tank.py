import pygame


class Tank:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = 300
        self.image = pygame.image.load("../media/tank.png")
