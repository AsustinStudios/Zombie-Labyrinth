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

from living_being import Living_being

# ==============================================================================
class Zombie(Living_being):
	""" The class that represents the zombies on the game"""

	# ==========================================================================
	def __init__(self, start_location=(600, 300), sprite_prefix='zombie', object_type='ZOMBIE'):
		Living_being.__init__(self, start_location, sprite_prefix, object_type)

		# ======================================================================
		""" Stats"""
		self.handedness = 0
		self.life = 50
		self.speed = 10
		self.strength = 40
		self.programming = 0
		self.data_sciencing = 0
