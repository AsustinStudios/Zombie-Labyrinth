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

from src.resources import load_sprite
from src.global_variables import NORTH, SOUTH, EAST, WEST

# ==============================================================================
class Game_object(pygame.sprite.Sprite):
	""" The super class that represents all objects on the game on the game"""

	# ==========================================================================
	def __init__(self, location, object_type):
		pygame.sprite.Sprite.__init__(self) # call Sprite initializer
		self.image, self.rect = load_sprite(object_type)
		self.rect = self.rect.move(location)
		self.object_type = object_type
		self.life = 100
		self.direction = SOUTH
		self.animation_count = 0

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		pass

	# ==========================================================================
	def receive_damage(self, damage):
		""" Receive damage, process it and apply it to life"""
		self.life -= damage

# ==============================================================================
class Bullet(Game_object):
	""" The super class that represents proyectiles in the game."""

	# ==========================================================================
	def __init__(self, start_location, direction, collision_group, speed=50,
					strength=10, object_type='bullet'):
		Game_object.__init__(self, start_location, object_type)

		position = start_location
		self.direction = direction
		self.image, a = load_sprite(self.object_type, None, self.direction)
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
				obj.receive_damage(self.strength)

	# ==========================================================================
	def move(self):
		""" Move around the being depending on the direction"""
		self.rect.move_ip(self.speed)

	# ==========================================================================
	def get_coordinate_speed(self, direction, speed):
		""" Receives a speed and returns the (x,y) px pair needed by the
		rect.move function to move at the received speed"""
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

