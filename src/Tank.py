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
        self.hit_box = pygame.Rect(self.x, self.y, 100, 100)
        self.can_go_left = True
        self.can_go_right = True
        self.can_go_up = True
        self.can_go_down = True

    def draw(self):
        self.screen.blit(self.scaled_image, (self.x, self.y))

    def move_left(self):
        if self.can_go_left:
            self.x -= self.speed

    def move_right(self):
        if self.can_go_right:
            self.x += self.speed

    def move_up(self):
        if self.can_go_up:
            self.y -= self.speed

    def move_down(self):
        if self.can_go_down:
            self.y += self.speed

    def get_hit_box(self):
        self.hit_box = pygame.Rect(self.x, self.y, 100, 100)

    def crashed_into_obstacle_from_right(self, obstacle):
        return (self.hit_box.collidepoint(obstacle.x + 100, obstacle.y)
                or self.hit_box.collidepoint(obstacle.x + 100, obstacle.y + 100))

    def crashed_into_obstacle_from_left(self, obstacle):
        return (self.hit_box.collidepoint(obstacle.x, obstacle.y)
                or self.hit_box.collidepoint(obstacle.x, obstacle.y + 100))

    def crashed_into_obstacle_from_top(self, obstacle):
        return (self.hit_box.collidepoint(obstacle.x, obstacle.y)
                or self.hit_box.collidepoint(obstacle.x + 100, obstacle.y))

    def crashed_into_obstacle_from_bottom(self, obstacle):
        return (self.hit_box.collidepoint(obstacle.x, obstacle.y + 100)
                or self.hit_box.collidepoint(obstacle.x + 100, obstacle.y + 100))
