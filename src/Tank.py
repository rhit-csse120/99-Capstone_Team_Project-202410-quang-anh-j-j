import pygame


class Tank:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("../media/tank.png")
        self.scaled_image = pygame.transform.scale(self.image, (100, 100))
        self.speed = 3
        self.has_exploded = False

    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed