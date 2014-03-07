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

import preferences

# ==============================================================================
global screen_center, allsprites, objects_group, preferences
screen_center = (600,300)
allsprites = pygame.sprite.OrderedUpdates()
objects_group = pygame.sprite.Group()
preferences = preferences.Preferences()

# ==============================================================================
global RIGHT, LEFT, NORTH, SOUTH, EAST, WEST

RIGHT = 0
LEFT = 1
NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'

# ==============================================================================
global GUN, NOT_GUN

COLD_WEAPON = 0
FIREARM = 1

# ==============================================================================
global UP, DOWN

UP = 2
DOWN = 3
