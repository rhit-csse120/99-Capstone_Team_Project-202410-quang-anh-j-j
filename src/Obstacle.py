import pygame
class Obstacle:
    def __init__(self, x, y, width, height, image):
        self.x = 200
        self.y = 250
        self.width = 10
        self.height = 20
        self.image = pygame.image.load("../media/pumpkin_1.png")
    def draw(self):
        