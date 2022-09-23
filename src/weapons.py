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
Date: 2013-11-26
"""

import pygame
from pygame.locals import *

from src.game_objects import Bullet
from src.global_variables import allsprites
# ==============================================================================
global COLD_WEAPON, FIREARM

COLD_WEAPON = 0
FIREARM = 1

# ==============================================================================
class Weapon():
    """ The class that represents the weapons in the game"""

    # ==========================================================================
    def __init__(self, type, strength, name):
        self.type = type
        self.strength = strength
        self.name = name

    # ==========================================================================
    def __str__(self):
        return self.name

# ==============================================================================
class Cold_weapon(Weapon):
    """ The class that represents the white arms in the game"""

    # ==========================================================================
    def __init__(self, strength=10, range=20, name='Cold_weapon'):
        Weapon.__init__(self, COLD_WEAPON, strength, name)
        self.range = range

# ==============================================================================
class Firearm(Weapon):
    """ The class that represents the firearms in the game"""


    # ==========================================================================
    def __init__(self, strength=10, name='Firearm'):
        Weapon.__init__(self, FIREARM, strength, name)

    # ==========================================================================
    def attack(self, rect, direction, collision_group):
        position = (rect[0], rect[1])
        allsprites.add(Bullet(position, direction, collision_group))
