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
                ,pymunk.Segment(space.static_body, (50, 500), (500, 500), 5)
                ,pymunk.Segment(space.static_body, (100, 450), (550, 450), 5)
                ,pymunk.Segment(space.static_body, (50, 400), (500, 400), 5)
                ,pymunk.Segment(space.static_body, (100, 350), (550, 350), 5)
                ,pymunk.Segment(space.static_body, (50, 210.8), (250, 210), 5)
                ,pymunk.Segment(space.static_body, (250, 300), (500, 300), 5)
                ,pymunk.Segment(space.static_body, (250, 300), (250, 210), 5)
                ,pymunk.Segment(space.static_body, (500, 200), (550, 200.5), 5)
                ,pymunk.Segment(space.static_body, (500, 200), (500, 100), 5)
                ,pymunk.Segment(space.static_body, (300, 100), (500, 100), 5)
                ,pymunk.Segment(space.static_body, (300, 100), (300, 200), 5)
                ]

blocks = [(165, 450), (465, 350)]
finish = (150,150)

