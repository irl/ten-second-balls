#
# Ten Second Balls
# Copyright (C) 2013 Iain Learmonth
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk.pygame_util import draw_space

class Universe:

    def __init__(self, level):
        # Initialisation
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Ludum Dare 27 - 10 Seconds - A thing by irl")
        self.clock = pygame.time.Clock()
        self.won = self.lost = False

        # Set up space
        self.space = space = pymunk.Space()
        space.gravity = (0.0, -900.0)

        # Set up walls
        space.add(level.get_universe_walls(space))

        space.add_collision_handler(2, 3, post_solve=self.activate_bomb)
        space.add_collision_handler(1, 2, post_solve=self.win)

        # Set up blocks
        for block in level.blocks:
            x, y = block
            self.add_block(x, y)

        # Set up finish
        x, y = level.finish
        self.add_finish(x, y)

    def add_block(self, x, y):
        inertia = pymunk.moment_for_circle(1, 0, 14, (0,0))
        body = pymunk.Body(1, inertia) 
        shape = pymunk.Circle(body, 14)
        body.position = x, y 
        shape.collision_type = 3
        shape.color = THECOLORS['purple']
        self.space.add(body, shape)
        return shape

    def add_finish(self, x, y):
        body = pymunk.Body(pymunk.inf, pymunk.inf)
        shape = pymunk.Circle(body, 25)
        body.position = x, y 
        shape.collision_type = 1
        shape.color = THECOLORS['yellow']
        self.space.add(body, shape)

    def tick(self):
        self.screen.fill(THECOLORS['black'])
        draw_space(self.screen, self.space)
        self.space.step(1/50.0)
        pygame.display.flip()
        self.clock.tick(50)

        dead_blocks = []

        for shape in self.space.shapes:
            if shape.collision_type > 5:
               shape.collision_type -= 1
            if shape.collision_type == 5:
               dead_blocks.append(shape)
        for shape in dead_blocks:
            self.space.remove(shape)

    def win(self, space, arbiter):
        print "YOU WIN!"
        self.won = True

    def activate_bomb(self, space, arbiter):
        print "Bomb activated"
        for shape in arbiter.shapes:
            if shape.collision_type == 3:
                shape.collision_type = 600
                shape.color = THECOLORS['red']

