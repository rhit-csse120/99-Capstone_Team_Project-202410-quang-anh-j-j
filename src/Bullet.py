import pygame


class Bullet:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.h_speed = 10
        self.v_speed = 0
        self.height = 10
        self.width = 8
        self.hit_by_tank = False
        self.hit_by_obstacles = False
        self.has_exploded = False
        self.color = "magenta"

    def draw(self):
        pygame.draw.line(self.screen, self.color,
                         (self.x, self.y),
                         (self.x + self.height, self.y),
                         self.width)

    def move(self):
        self.x = self.x - self.h_speed
        self.y = self.y + self.v_speed

    def explode(self):
        self.has_exploded = True

import pygame


class Bullet:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.h_speed = 10
        self.v_speed = 0
        self.height = 6
        self.width = 4
        self.hit_by_tank = False
        self.hit_by_obstacles = False
        self.has_exploded = False
        self.color = "magenta"

    def draw(self):
        pygame.draw.line(self.screen, self.color,
                         (self.x, self.y),
                         (self.x + self.height, self.y),
                         self.width)

    def move(self):
        self.x = self.x + self.h_speed
        self.y = self.y + self.v_speed

    def explode(self):
        self.has_exploded = True

