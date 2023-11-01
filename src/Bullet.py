import pygame


class Bullet:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.h_speed = 10
        self.v_speed = 0
        self.hit_by_tank = False
        self.hit_by_obstacles = False

    def draw(self):
        pygame.draw.line(self.screen, "magenta",
                         (self.x, self.y),
                         (self.x + 5, self.y))

    def move(self):
        self.x = self.x + self.h_speed
        self.y = self.y + self.v_speed

    def explode(self):
        pass

