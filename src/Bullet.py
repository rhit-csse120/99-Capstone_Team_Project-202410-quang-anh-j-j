import pygame
from Obstacle import Obstacle
from Obstacles import Obstacles


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

    def is_hit_by_obstacles(self, obstacle: Obstacle):
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.y,
                                    obstacle.hit_box.width, obstacle.hit_box.height)
        bullet_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(obstacle_rect)

    # def is_hit_by_tanks(self, obstacle: Obstacle):
    #     obstacle_rect = pygame.Rect(obstacle.x, obstacle.y,
    #                                 obstacle.hit_box.width, obstacle.hit_box.height)
    #     bullet_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #     return bullet_rect.collidepoint(obstacle_rect)

    def explode(self):
        self.has_exploded = True

