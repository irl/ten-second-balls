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

import pymunk

def get_universe_walls(space):
    return [pymunk.Segment(space.static_body, (50, 50), (50, 550), 5)
                ,pymunk.Segment(space.static_body, (50, 550), (550, 550), 5)
                ,pymunk.Segment(space.static_body, (550, 550), (550, 50), 5)
                ,pymunk.Segment(space.static_body, (50, 50), (550, 50), 5)
                ,pymunk.Segment(space.static_body, (100, 550), (100, 100), 5)
                ,pymunk.Segment(space.static_body, (300, 500), (300, 50), 5)
                ,pymunk.Segment(space.static_body, (150, 100), (300, 100), 5)
                ,pymunk.Segment(space.static_body, (100, 150), (250, 150), 5)
                ,pymunk.Segment(space.static_body, (150, 200), (300, 200), 5)
                ,pymunk.Segment(space.static_body, (100, 250), (250, 250), 5)
                ,pymunk.Segment(space.static_body, (150, 300), (300, 300), 5)
                ,pymunk.Segment(space.static_body, (100, 350), (250, 350), 5)
                ,pymunk.Segment(space.static_body, (150, 400), (300, 400), 5)
                ,pymunk.Segment(space.static_body, (100, 450), (250, 450), 5)
                ,pymunk.Segment(space.static_body, (150, 500), (300, 500), 5)
                ,pymunk.Segment(space.static_body, (350, 550), (350, 190), 5)
                ,pymunk.Segment(space.static_body, (350, 150), (350, 50), 5)
                ,pymunk.Segment(space.static_body, (550, 150), (350, 150), 5)
                ]

blocks = [(100,150), (100, 200), (100, 250), (200, 500), (250,550), (300, 550), (350, 550)]
finish = (550,550)

