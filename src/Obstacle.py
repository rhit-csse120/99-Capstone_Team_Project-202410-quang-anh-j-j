import random

import pygame


class Obstacle:
    def __init__(self, screen, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.image_scale = pygame.transform.scale(self.image, (100, 100))
        self.screen = screen
        self.hit_box = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self):
        self.screen.blit(self.image_scale, (self.x, self.y))
