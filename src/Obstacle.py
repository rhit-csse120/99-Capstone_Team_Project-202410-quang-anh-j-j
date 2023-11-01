import random

import pygame


class Obstacle:
    def __init__(self, screen):
        self.x = 200
        self.y = 250
        self.image = pygame.image.load("../media/pumpkin_1.png")
        # self.image_1 = pygame.image.load("../media/pumpkin_2.png")
        # self.image_2 = pygame.image.load("../media/ghost.png")
        self.image_scale = pygame.transform.scale(self.image, (100, 100))
        # self.image_scale1 = pygame.transform.scale(self.image_1, (100, 100))
        # self.image_scale2 = pygame.transform.scale(self.image_2, (100, 100))
        # self.list = [self.image_scale, self.image_scale1, self.image_scale2]
        # self.x = random.ra
        self.screen = screen
        self.hit_box = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self):
        self.screen.blit(self.image_scale, (self.x, self.y))
