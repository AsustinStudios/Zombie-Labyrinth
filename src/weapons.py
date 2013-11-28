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

import geometry
from global_variables import *
from resources import *
from game_object import Game_object

# ==============================================================================
class Weapon():
	""" The class that represents the weapons in the game"""

	# ==========================================================================
	def __init__(self, type):
		self.type = type

# ==============================================================================
class Cold_weapon(Weapon):
	""" The class that represents the white arms in the game"""

	# ==========================================================================
	def __init__(self, strength=10, range=20):
		Weapon.__init__(self, COLD_WEAPON)
		self.range = range
		self.strength = strength

# ==============================================================================
class Firearm(Weapon):
	""" The class that represents the firearms in the game"""

	# ==========================================================================
	def __init__(self, strength=10):
		Weapon.__init__(self, FIREARM)
		self.strength = strength

	# ==========================================================================
	def attack(self, rect, direction, collision_group):
		position = (rect[0], rect[1])
		allsprites.add(Bullet(position, direction, collision_group))


# ==============================================================================
class Bullet(Game_object):

	# ==========================================================================
	def __init__(self, start_location, direction, collision_group, speed=50,
					strength=10, sprite_prefix='bullet', object_type='BULLET'):
		Game_object.__init__(self, start_location,
							'%s_%s' % (sprite_prefix, direction), object_type)

		position = start_location
		self.speed = self.get_coordinate_speed(direction, speed)
		self.collision_group = collision_group
		self.strength = strength

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		self.move()
		self.process_collisions()

	# ==========================================================================
	def process_collisions(self):
		collision_list = pygame.sprite.spritecollide(self,
													self.collision_group, False)
		if len(collision_list) != 0:
			self.kill()
			for obj in collision_list:
				print self
				print "Inflicting %i" % self.strength
				obj.receive_damage(self.strength)

	# ==========================================================================
	def move(self):
		""" Move around the being depending on the direction"""
		self.rect.move_ip(self.speed)

	# ==========================================================================
	def get_coordinate_speed(self, direction, speed):
		x, y = 0, 0

		if direction == NORTH:
			y = -speed/10
		elif direction == EAST:
			x = speed/10
		elif direction == SOUTH:
			y = speed/10
		elif direction == WEST:
			x = -speed/10

		return (x, y)

