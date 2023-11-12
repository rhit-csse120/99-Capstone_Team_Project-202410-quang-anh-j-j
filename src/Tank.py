import math
import time

import pygame

from Bullet import Bullet
from Bullets import Bullets


class Tank:
    def __init__(self, screen, x, y, angle, bullets):
        self.screen = screen
        self.x = x
        self.y = y
        self.height = 75
        self.width = 75
        self.angle = angle - 90
        image = pygame.image.load("../media/tank.png")
        self.scaled_image = pygame.transform.scale(image, (self.height, self.width))
        self.og_image = pygame.transform.rotate(self.scaled_image, angle)
        self.image = self.og_image
        self.speed = 3
        self.has_exploded = False
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        # self.can_go_left = True
        # self.can_go_right = True
        # self.can_go_up = True
        # self.can_go_down = True
        self.bullets = bullets
        self.angle_for_turning = 0
        self.pew_shooting = pygame.mixer.Sound("../media/Pew-pew.mp3")
        self.health = 100
        self.can_shoot = True
        self.a = True
        self.explode_music = pygame.mixer.Sound("../media/hq-explosion-6288.mp3")


    def draw(self):
        # if self.angle % 45 == 0 and self.angle % 90 != 0:
        #     self.hit_box = self.image.get_rect(center=(self.x + self.width / math.sqrt(2),
        #                                                self.y + self.height / math.sqrt(2)))
        #     self.hit_box = self.image.get_rect(center=(self.x + self.width / math.sqrt(2),
        #                                                self.y + self.height / math.sqrt(2)))
        # else:
        #     self.hit_box = self.image.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        # self.screen.blit(self.image, self.hit_box.center)

        if self.angle % 45 == 0 and self.angle % 90 != 0:
            self.hit_box = self.image.get_rect(center=(self.x, self.y))
        else:
            self.hit_box = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.hit_box.center)

    def move_forward(self):
        self.x += math.cos(self.angle * math.pi / 180) * self.speed
        self.y -= math.sin(self.angle * math.pi / 180) * self.speed

    def move_backward(self):
        self.x -= math.cos(self.angle * math.pi / 180) * self.speed
        self.y += math.sin(self.angle * math.pi / 180) * self.speed

    def turn_left(self):
        self.angle += 45
        self.angle_for_turning += 45
        self.image = pygame.transform.rotate(self.og_image, self.angle_for_turning)
        if self.angle_for_turning % 45 == 0 and self.angle_for_turning % 90 != 0:
            self.x -= math.sqrt(2) / 4 * self.width
            self.y -= math.sqrt(2) / 4 * self.height
        else:
            self.x += math.sqrt(2) / 4 * self.width
            self.y += math.sqrt(2) / 4 * self.height

    def turn_right(self):
        self.angle -= 45
        self.angle_for_turning -= 45
        self.image = pygame.transform.rotate(self.og_image, self.angle_for_turning)
        if self.angle_for_turning % 45 == 0 and self.angle_for_turning % 90 != 0:
            self.x -= math.sqrt(2) / 4 * self.width
            self.y -= math.sqrt(2) / 4 * self.height
        else:
            self.x += math.sqrt(2) / 4 * self.width
            self.y += math.sqrt(2) / 4 * self.height

    def get_hit_box(self):
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
        if self.can_shoot:
            self.bullets.add_bullets(Bullet(self.screen,
                                            self.hit_box.center[0]
                                            + self.hit_box.width / 2 * (math.cos(self.angle * math.pi / 180) + 1),
                                            self.hit_box.center[1]
                                            - self.hit_box.height / 2 * (math.sin(self.angle * math.pi / 180) - 1),
                                            self.angle, self))
            self.pew_shooting.play()

    # def explode(self, bullet):
    #     if bullet.tank is not self:
    #         self.has_exploded = True
    #     print(self, bullet)

    def explode(self):
        self.has_exploded = True

    def remove_dead_tank(self):

        # self.explode_music.play(1)
        if self.has_exploded:
            self.can_shoot = False

            del self

    def music(self):
        while self.has_exploded == True:
            self.explode_music.play(1)

    def handle_explosions(self, tank, bullets: Bullets):
        self.bullets = bullets
        if tank.health == 0:
            tank.explode()
            tank.remove_dead_tank()

        for k in range(len(self.bullets.list_of_bullets) - 1, -1, -1):
            bullet = self.bullets.list_of_bullets[k]
            bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
            tank_rect = pygame.Rect(tank.x + 12.5, tank.y + 12.5, 50, 50)
            print(bullet_rect)
            print(tank_rect)
            print(self.x, self.y)
            if bullet_rect.colliderect(tank_rect):
                bullet.explode()
                self.bullets.remove_dead_bullet()
                print("jenfjnesf")
                if tank.health >= 20:
                    tank.health = tank.health - 20
                    self.explode_music.play()
                    tank.display_health()

    def display_health(self):
        if self.health > 0:
            pygame.draw.rect(self.screen, "black", pygame.Rect(self.x, self.y - 25, 75, 20), 3)
            pygame.draw.rect(self.screen, "green",
                             pygame.Rect(self.x + 3, self.y - 25 + 3, (75 - 3 * 2) * (self.health / 100), 14))
            pygame.draw.rect(self.screen, "red",
                             pygame.Rect(self.x + 75 - 3 - (100 - self.health) * (75 - 6) / 100, self.y - 25 + 3,
                                         (100 - self.health) * (75 - 6) / 100, 14))
