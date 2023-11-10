import pygame.image


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen

        font_1 = pygame.font.SysFont("Player_1_Win", 100)
        self.caption1 = font_1.render("Player_1_win", True, (255, 0, 255))

        font_2 = pygame.font.SysFont("PLayer_2_win", 100)
        caption2 = font_2.render("Player_2_win", True, (255, 0, 255))

    def draw(self):
        self.screen.blit(self.caption1, (550, 350))
