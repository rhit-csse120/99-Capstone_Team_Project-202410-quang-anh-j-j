import pygame
from Bullet import Bullet
# from Tank import Tank
from Obstacle import Obstacle


class Bullets:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.list_of_bullets = []

    def add_bullets(self, bullet: Bullet):
        self.list_of_bullets.append(bullet)

    def draw(self):
        for bullet in self.list_of_bullets:
            bullet.draw()

    def move(self):
        for bullet in self.list_of_bullets:
            bullet.move()

    def remove_dead_bullet(self):
        for bullet in self.list_of_bullets:
            if bullet.has_exploded is True or bullet.hit_by_tank is True or bullet.hit_by_obstacles is True:
                del bullet

    # def handle_explosions(self, tank: Tank):
    #     pass
