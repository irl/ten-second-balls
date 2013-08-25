#!/usr/bin/env python
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

import sys, pygame
from pygame.locals import *
from universe import Universe
from player import Player
import level1

def main():
    dx = dy = jump = 0

    running = True

    universe = Universe(level1)
    player = Player(universe)

    while running:

        # Process events
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

        # Make player move
        player.act(dx, dy)

        # Jump limiting
        dy = 0
        if jump > 0:
            jump -= 1

        # SIMULATE!
        universe.tick()

if __name__ == '__main__':
    sys.exit(main())

