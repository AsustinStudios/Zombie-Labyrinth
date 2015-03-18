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

import pygame
from pygame.locals import *

#from resources import *
import resources

# ==============================================================================
class Game_object(pygame.sprite.Sprite):
	""" The super class that represents all objects on the game on the game"""

	# ==========================================================================
	def __init__(self, location, object_type):
		pygame.sprite.Sprite.__init__(self) # call Sprite initializer
		self.image, self.rect = resources.load_sprite(object_type)
		self.rect = self.rect.move(location)
		self.object_type = object_type
		self.life = 100
		self.animation_count = 0

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		pass

	# ==========================================================================
	def receive_damage(self, damage):
		""" Receive damage, process it and apply it to life"""
		self.life -= damage
