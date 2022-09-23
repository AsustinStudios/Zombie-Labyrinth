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
Date: 2014-03-06
"""
from src.input import get_direction_from_look
from src.global_variables import allsprites, preferences

# ==============================================================================
def look():
    for dude in allsprites:
        if dude.object_type == 'zombie':
            dude.look((preferences.player.rect[0], preferences.player.rect[1]))

# ==============================================================================
def dumb_chase():
    for dude in allsprites:
        if dude.object_type == 'zombie':
            dude.look((preferences.player.rect[0], preferences.player.rect[1]))
            dude.move(get_direction_from_look(dude.direction))
