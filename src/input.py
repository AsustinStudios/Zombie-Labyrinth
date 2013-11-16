#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#    Zombie Labyrinth
#    Copyright (C) 2013 Roberto Lapuente topo@asustin.net
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
#
#    For more information send an e-mail to topo@asustin.net.

from pygame.locals import *

# ==============================================================================
global RIGHT, LEFT, UP, DOWN

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

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