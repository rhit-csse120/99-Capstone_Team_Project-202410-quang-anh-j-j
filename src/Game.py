"""
The  Game (model)  file for the Model-View-Controller architecture for our game.
1. It constructs all the objects specific to this game.
2. Its   draw_game   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to draw themselves.
3. Its   run_one_cycle   method is called repeatedly by the main game loop and
   typically asks each of the Game's objects to do whatever needs to happen
   independently of events / user-input.

Team members:
Anh Ngo
J.J. Moe
Quang Dao
"""
# DONE: Put the names of your entire team in the above doc-string.

import pygame
import math
from Bullets import Bullets
from Obstacles import Obstacles
# DONE: Put each class in its own module, using the same name for both.
#  Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
from Tank import Tank
from winning_screen import Scoreboard


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # TODO: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        self.bullets = Bullets(self.screen)
        self.tank_1 = Tank(self.screen, 100, (self.screen.get_height() - 75) / 2, 90, self.bullets)
        self.tank_2 = Tank(self.screen, self.screen.get_width() - 250,
                           (self.screen.get_height() - 75) / 2, -90, self.bullets)
        self.obstacles = Obstacles(self.screen)
        self.background_music = pygame.mixer.Sound("../media/bouncy-ball-55955.mp3")
        self.scoreboard = Scoreboard(screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.fighter.draw():
        if self.tank_1.has_exploded is not True:
            self.tank_1.draw()
        if self.tank_2.has_exploded is not True:
            self.tank_2.draw()
        # self.tank_1.draw()
        # self.tank_2.draw()
        self.obstacles.draw()
        self.bullets.draw()
        if self.tank_1.has_exploded:
            self.scoreboard.draw_2()
        if self.tank_2.has_exploded:
            self.scoreboard.draw_1()

        pygame.draw.rect(self.screen, "black", pygame.Rect(self.tank_1.x, self.tank_1.y,
                                                           self.tank_1.width, self.tank_1.height), 5)
        pygame.draw.rect(self.screen, "black", pygame.Rect(self.tank_2.x, self.tank_2.y,
                                                           self.tank_2.width, self.tank_2.height), 5)
        self.tank_1.display_health()
        self.tank_2.display_health()
        if self.tank_1.angle % 45 == 0 and self.tank_1.angle % 90 != 0:
            pygame.draw.rect(self.screen, "red", pygame.Rect(self.tank_1.x + 12.5 + 37.5 * (math.sqrt(2) - 1), self.tank_1.y + 12.5 + 37.5 * (math.sqrt(2) - 1), 50, 50))
        else:
            pygame.draw.rect(self.screen, "red", pygame.Rect(self.tank_1.x + 12.5, self.tank_1.y + 12.5, 50, 50))

        if self.tank_2.angle % 45 == 0 and self.tank_2.angle % 90 != 0:
            pygame.draw.rect(self.screen, "red", pygame.Rect(self.tank_2.x + 12.5 + 37.5 * (math.sqrt(2) - 1),
                                                             self.tank_2.y + 12.5 + 37.5 * (math.sqrt(2) - 1), 50, 50))
        else:
            pygame.draw.rect(self.screen, "red", pygame.Rect(self.tank_2.x + 12.5, self.tank_2.y + 12.5, 50, 50))

        pygame.draw.circle(self.screen, "magenta", (self.tank_1.x + 12.5, self.tank_1.y), 5, 5)
        pygame.draw.circle(self.screen, "magenta", (self.tank_2.x + 12.5, self.tank_2.y), 5, 5)

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)

        # self.background_music.play()

        self.bullets.move()
        self.bullets.handle_explosions_obstacles(self.obstacles)

        self.tank_1.handle_explosions(self.tank_2, self.tank_1.bullets)
        self.tank_2.handle_explosions(self.tank_1, self.tank_2.bullets)


        for obstacle in self.obstacles.obstacles:
            self.tank_1.get_hit_box()
            self.tank_2.get_hit_box()

            # if self.tank_1.crashed_into_obstacle_from_left(obstacle):
            #     self.tank_1.can_go_right = False
            # else:
            #     self.tank_1.can_go_right = True
            # if self.tank_1.crashed_into_obstacle_from_right(obstacle):
            #     self.tank_1.can_go_left = False
            # else:
            #     self.tank_1.can_go_left = True
            # if self.tank_1.crashed_into_obstacle_from_top(obstacle):
            #     self.tank_1.can_go_down = False
            # else:
            #     self.tank_1.can_go_down = True
            # if self.tank_1.crashed_into_obstacle_from_bottom(obstacle):
            #     self.tank_1.can_go_up = False
            # else:
            #     self.tank_1.can_go_up = True
            #
            #
            # if self.tank_2.crashed_into_obstacle_from_left(obstacle):
            #     self.tank_2.can_go_right = False
            # else:
            #     self.tank_2.can_go_right = True
            # if self.tank_2.crashed_into_obstacle_from_right(obstacle):
            #     self.tank_2.can_go_left = False
            # else:
            #     self.tank_2.can_go_left = True
            # if self.tank_2.crashed_into_obstacle_from_top(obstacle):
            #     self.tank_2.can_go_down = False
            # else:
            #     self.tank_2.can_go_down = True
            # if self.tank_2.crashed_into_obstacle_from_bottom(obstacle):
            #     self.tank_2.can_go_up = False
            # else:
            #     self.tank_2.can_go_up = True
