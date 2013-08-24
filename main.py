#!/usr/bin/env python27
#
#   Ten Second Balls
#   Copyright (C) 2013  Iain Learmonth
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import sys, random
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk.pygame_util import draw_space
from universe import Universe

dx = dy = jump = 0

dead = []

def win(space, arbiter):
    print "YOU WIN!"
    sys.exit()

def activate_bomb(space, arbiter):
    print "Bomb activated"
    for shape in arbiter.shapes:
        if shape.collision_type == 3:
            shape.collision_type = 600
            shape.color = THECOLORS['red']
                

def add_finish(space, x, y):
    body = pymunk.Body(pymunk.inf, pymunk.inf)
    shape = pymunk.Circle(body, 25)
    body.position = x, y 
    shape.collision_type = 1
    shape.color = THECOLORS['yellow']
    space.add(body, shape)
    return (body, shape)

def add_player(space):
    mass = 1
    radius = 14
    inertia = pymunk.moment_for_circle(mass, 0, radius, (dx,0))
    body = pymunk.Body(mass, inertia) 
    body.position = 65, 550
    body.friction = 0.6
    shape = pymunk.Circle(body, radius)
    shape.collision_type = 2
    shape.color = THECOLORS['blue']
    space.add(body, shape)
    return (body, shape)

def draw_player(screen, player):
    p = int(player.body.position.x), 600-int(player.body.position.y)
    pygame.draw.circle(screen, THECOLORS["blue"], p, int(player.radius), 2)

def main():
    global dx, dy, jump, dead


    running = True

    universe = Universe()

#    player_body, player_shape = add_player(space)

    universe.add_block(165, 450)
    universe.add_block(465, 350)

#    finish_body, finish_shape = add_finish(space, 150, 150)

#    space.add_collision_handler(2, 3, post_solve=activate_bomb)
#    space.add_collision_handler(1, 2, post_solve=win)

    while running:

        dy = 0

        if jump > 0:
            jump -= 1

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                break
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
                break
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    dx = 10
                if event.key == K_a:
                    dx = -10
                if event.key == K_w:
                    if jump == 0:
                        dy = 350
                        jump = 35
            elif event.type == KEYUP:
                if event.key == K_d or event.key == K_a:
                    dx = 0
                if event.key == K_w:
                    dy = 0

#        player_body.apply_impulse((dx,dy))



#        for shape in space.shapes:
#            if shape.collision_type > 5:
#               shape.collision_type -= 1
#            if shape.collision_type == 5:
#               dead.append(shape)

#        for shape in dead:
#            space.remove(shape)
#        dead = []

        universe.tick()



if __name__ == '__main__':
    sys.exit(main())


