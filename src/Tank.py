import pygame
import math
from Bullet import Bullet


def blitRotate2(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)
class Tank:
    def __init__(self, screen, x, y, angle, bullets):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = 75
        self.width = 75
        self.angle = angle - 90
        image = pygame.image.load("../media/tank.png")
        scaled_image = pygame.transform.scale(image, (self.height, self.width))
        self.image = pygame.transform.rotate(scaled_image, angle)
        self.speed = 3
        self.has_exploded = False
        self.hit_box = pygame.Rect(self.x, self.y, 100, 100)
        # self.can_go_left = True
        # self.can_go_right = True
        # self.can_go_up = True
        # self.can_go_down = True
        self.bullets = bullets

    def draw(self):
        self.screen.blit(self.image, self.hit_box)

    def move_forward(self):
        self.x += math.cos(self.angle * math.pi / 180) * self.speed
        self.y += math.sin(self.angle * math.pi / 180) * self.speed

    def move_backward(self):
        self.x -= math.cos(self.angle * math.pi / 180) * self.speed
        self.y -= math.sin(self.angle * math.pi / 180) * self.speed

    def turn_left(self):
        self.angle -= 45
        blitRotate2(self.screen, self.image, (self.x, self.y), -45)
        print("ya")

    def turn_right(self):
        self.angle += 45
        # self.scaled_and_rotated_image = pygame.transform.rotate(self.scaled_and_rotated_image, 90)

    # def move_left(self):
    #     if self.can_go_left:
    #         self.x -= self.speed
    #
    # def move_right(self):
    #     if self.can_go_right:
    #         self.x += self.speed
    #
    # def move_up(self):
    #     if self.can_go_up:
    #         self.y -= self.speed
    #
    # def move_down(self):
    #     if self.can_go_down:
    #         self.y += self.speed

    def get_hit_box(self):
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        return self.hit_box

    # def crashed_into_obstacle_from_right(self, obstacle):
    #     return (self.hit_box.collidepoint(obstacle.x + 100, obstacle.y)
    #             or self.hit_box.collidepoint(obstacle.x + 100, obstacle.y + 100))
    #
    # def crashed_into_obstacle_from_left(self, obstacle):
    #     return (self.hit_box.collidepoint(obstacle.x, obstacle.y)
    #             or self.hit_box.collidepoint(obstacle.x, obstacle.y + 100))
    #
    # def crashed_into_obstacle_from_top(self, obstacle):
    #     return (self.hit_box.collidepoint(obstacle.x, obstacle.y)
    #             or self.hit_box.collidepoint(obstacle.x + 100, obstacle.y))
    #
    # def crashed_into_obstacle_from_bottom(self, obstacle):
    #     return (self.hit_box.collidepoint(obstacle.x, obstacle.y + 100)
    #             or self.hit_box.collidepoint(obstacle.x + 100, obstacle.y + 100))

    def shoot(self):
        self.bullets.add_bullets(Bullet(self.screen,
                                        self.x + self.width/2 + math.cos(self.angle),
                                        self.y + self.height/2 + math.sin(self.angle)))
