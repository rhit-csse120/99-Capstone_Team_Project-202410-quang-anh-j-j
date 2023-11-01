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



class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # TODO: Store whatever YOUR game needs, perhaps something like this:
        #     self.missiles = Missiles(self.screen)
        #     self.fighter = Fighter(self.screen, self.missiles)
        self.tank_1 = Tank(self.screen, 100, 300)
        self.tank_2 = Tank(self.screen, 900, 300)
        self.obstacles = Obstacles(self.screen)

    def draw_game(self):
        """ Ask all the objects in the game to draw themselves. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.fighter.draw()
        self.tank_1.draw()
        self.tank_2.draw()
        self.obstacles.draw()

    def run_one_cycle(self):
        """ All objects that do something at each cycle: ask them to do it. """
        # TODO: Use something like the following, but for objects in YOUR game:
        #     self.missiles.move()
        #     self.missiles.handle_explosions(self.enemies)
