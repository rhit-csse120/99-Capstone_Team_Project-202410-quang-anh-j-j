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

# DONE: Put each class in its own module, using the same name for both.
#  Then use statements like the following, but for YOUR classes in YOUR modules:
#     from Fighter import Fighter
from Tank import Tank
from Obstacles import Obstacles
from Bullets import Bullets


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # DONE: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        self.bullets = Bullets(self.screen)
        self.tank_1 = Tank(self.screen, 100, (self.screen.get_height() - 75) / 2, 90, self.bullets)
        self.tank_2 = Tank(self.screen, self.screen.get_width() - 250,
                           (self.screen.get_height() - 75) / 2, -90, self.bullets)
        self.obstacles = Obstacles(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # DONE: Use something like the following, but for objects in YOUR game:
        #     self.fighter.draw()
        self.tank_1.draw()
        self.tank_2.draw()
        self.obstacles.draw()
        self.bullets.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # DONE: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)

        self.bullets.move()
        self.bullets.handle_explosions_obstacles(self.obstacles)

        # pressed_keys = pygame.key.get_pressed()
        # for obstacle in self.obstacles.obstacles:
        #     self.tank_1.get_hit_box()
        #     self.tank_2.get_hit_box()
        #     self.tank_1.can_go_forward = True
        #     self.tank_2.can_go_forward = True
        #     self.tank_1.can_go_forward = False
        #     self.tank_2.can_go_forward = False
        #     if self.tank_1.get_hit_box().colliderect(obstacle.hit_box) and pressed_keys[pygame.K_w]:
        #         self.tank_1.can_go_forward = False
        #     if self.tank_2.get_hit_box().colliderect(obstacle.hit_box) and pressed_keys[pygame.K_UP]:
        #         self.tank_2.can_go_forward = False
        #     if self.tank_1.get_hit_box().colliderect(obstacle.hit_box) and pressed_keys[pygame.K_s]:
        #         self.tank_1.can_go_backward = False
        #     if self.tank_2.get_hit_box().colliderect(obstacle.hit_box) and pressed_keys[pygame.K_DOWN]:
        #         self.tank_2.can_go_backward = False
