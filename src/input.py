#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#    Zombie Labyrinth
#    Copyright (C) 2013 Asustin Studios studios@asustin.net
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Author: Roberto Lapuente Romo
E-mail: topo@asustin.net
Date: 2013-11-06
"""

from pygame.locals import K_a, K_d, K_DOWN, K_LEFT, K_RIGHT, K_s, K_UP, K_w

from src.global_variables import RIGHT, LEFT, UP, DOWN
from src.global_variables import NORTH, SOUTH, EAST, WEST

# ==============================================================================
def get_directions(pressed_keys):
    directions = {RIGHT:False, LEFT:False, UP:False, DOWN:False, }
    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        directions[RIGHT] = True
    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
        directions[LEFT] = True
    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
        directions[DOWN] = True
    if pressed_keys[K_w] or pressed_keys[K_UP]:
        directions[UP] = True
    return directions

# ==============================================================================
def get_direction_from_look(look):
    directions = {RIGHT:False, LEFT:False, UP:False, DOWN:False, }
    if look == EAST:
        directions[RIGHT] = True
    if look == WEST:
        directions[LEFT] = True
    if look == SOUTH:
        directions[DOWN] = True
    if look == NORTH:
        directions[UP] = True
    return directions
