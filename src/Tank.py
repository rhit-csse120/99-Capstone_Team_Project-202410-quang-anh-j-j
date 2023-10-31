import pygame


class Tank:
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = 300
        self.image = pygame.image.load("../media/tank.png")
        self.speed = 5
        self.has_exploded = False

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed