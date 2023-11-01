import pygame


class Obstacle:
    def __init__(self, screen, image):
        self.x = 200
        self.y = 250
        self.width = 10
        self.height = 20
        self.image = pygame.image.load("../media/pumpkin_1.png")
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

