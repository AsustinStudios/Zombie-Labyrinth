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


import math


def delta(p1, p2):
    """Return a (x, y) coordenate with the distance in each coordenate between p1 and p2."""
    delta_x = p2[0] - p1[0]
    delta_y = p2[1] - p1[1]

    return (delta_x, delta_y)


def angle_between(p1, p2) -> float:
    """Return the angle in degrees between p1 and p2."""
    x, y = delta(p1, p2)
    angle = math.degrees(math.atan2(y, x))

    return -angle


def distance(p1, p2) -> float:
    """Return the distance between p1 and p2."""
    x, y = delta(p1, p2)
    a = y * y
    b = x * x
    c = math.sqrt(a + b)

    return c
