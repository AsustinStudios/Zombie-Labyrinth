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
Date: 2013-11-05
"""

import pygame
from pygame.locals import *

from living_being import Living_being

# ==============================================================================
class Human(Living_being):
	""" The class that represents the human player on the game"""

	# ==========================================================================
	def __init__(self, start_location=(600, 300), sprite_prefix='human', object_type='HUMAN'):
		Living_being.__init__(self, start_location, sprite_prefix, object_type)

		# ======================================================================
		""" Permanent Stats"""
		self.handedness = 0
		self.melee_range = 10
		self.life = 100

		""" Trainable Stats"""
		self.speed = 20
		self.strength = 20
		self.programming = 15
		self.data_sciencing = 15
