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
        # construct obstacle
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
        # construct the field
        self.image1 = pygame.image.load("../media/obstacle 1.png")
        self.image2 = pygame.image.load("../media/obstacle 2.png")
        self.image3 = pygame.image.load("../media/obstacle 3.png")
        self.image4 = pygame.image.load("../media/obstacle 4.png")
        self.list = [self.image1, self.image2, self.image3, self.image4]
        self.x = 20
        self.y = 20
        self.field = []
        for k in range(2):
            for i in range(8):
                self.field.append(Obstacle(screen, self.x, self.y, self.list[k]))
                self.y += 100
            self.x += 300

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()
        for obstacle_1 in self.field:
            obstacle_1.draw()
