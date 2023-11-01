import random

import pygame

from Obstacle import Obstacle


class Obstacles:
    def __init__(self, screen):
        self.image_1 = pygame.image.load("../media/pumpkin_1.png")
        self.image_2 = pygame.image.load("../media/pumpkin_2.png")
        self.image_3 = pygame.image.load("../media/ghost.png")
        self.list_image = [self.image_1, self.image_2, self.image_3]
        self.x = 300
        self.y = 100
        self.obstacles = []

        for k in range(2):
            for k in range(2):
                self.a = random.randint(0, 2)
                self.obstacles.append(Obstacle(screen, self.x, self.y, self.list_image[self.a]))
                self.y += 90
            self.x += 500
            self.y = 100
        self.y = 450
        self.x = 300

        for k in range(2):
            for k in range(2):
                self.a = random.randint(0, 2)
                self.obstacles.append(Obstacle(screen, self.x, self.y, self.list_image[self.a]))
                self.y += 90
            self.x += 500
            self.y = 450

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()
