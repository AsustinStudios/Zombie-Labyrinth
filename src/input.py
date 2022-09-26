#!/usr/bin/env python3
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
E-mail: roberto@lapuente.me
Date: 2013-11-06
"""

from pygame.locals import K_a, K_d, K_DOWN, K_LEFT, K_RIGHT, K_s, K_UP, K_w

from src.constants import Direction


def get_directions(pressed_keys):
    directions = {Direction.right: False, Direction.left: False, Direction.up: False, Direction.down: False}
    if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
        directions[Direction.right] = True
    if pressed_keys[K_a] or pressed_keys[K_LEFT]:
        directions[Direction.left] = True
    if pressed_keys[K_s] or pressed_keys[K_DOWN]:
        directions[Direction.down] = True
    if pressed_keys[K_w] or pressed_keys[K_UP]:
        directions[Direction.up] = True
    return directions


def get_direction_from_look(look):
    directions = {Direction.right: False, Direction.left: False, Direction.up: False, Direction.down: False}
    if look == Direction.east:
        directions[Direction.right] = True
    if look == Direction.west:
        directions[Direction.left] = True
    if look == Direction.south:
        directions[Direction.down] = True
    if look == Direction.north:
        directions[Direction.up] = True
    return directions
