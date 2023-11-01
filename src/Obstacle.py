import pygame


class Obstacle:
    def __init__(self, screen):
        self.x = 200
        self.y = 250
        self.image = pygame.image.load("../media/pumpkin_1.png")
        self.image_scale = pygame.transform.scale(self.image, (100, 100))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image_scale, (self.x, self.y))
