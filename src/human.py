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

import pygame
from pygame.locals import *

from abstract_game_objects import Living_being

# ==============================================================================
class Human(Living_being):
	""" The class that represents the human player on the game"""
	def __init__(self, start_location=(600, 300), colission_group=None, object_type='HUMAN', sprite_prefix='human', speed=3):
		Living_being.__init__(self, start_location, colission_group, object_type, sprite_prefix, speed)
