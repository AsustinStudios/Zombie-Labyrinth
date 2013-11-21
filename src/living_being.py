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
Date: 2013-11-15
"""

import pygame
from pygame.locals import *

import geometry
from input import *
from resources import *
from abstract_game_objects import Game_object

# ==============================================================================
global RIGHT, LEFT

RIGHT = 0
LEFT = 1

# ==============================================================================
class Living_being(Game_object):
	""" The class that represents all the living entities in the game"""

	# ==========================================================================
	def __init__(self, start_location=(50, 50), sprite_prefix='living_being', object_type='LIVING'):
		Game_object.__init__(self, start_location, sprite_prefix, object_type)
		self.collision_group = None

		# ======================================================================
		""" Stats"""
		self.handedness = 0
		self.life = 100
		self.speed = 20
		self.strength = 20
		self.programming = 0
		self.data_sciencing = 0

		# ======================================================================
		""" Inventory"""
		self.weapons = {0:None, 1:None}
		self.inventory = []

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		self.process_collisions()
		self.monitor_life()

	# ==========================================================================
	def move(self, directions):
		""" Move around the being depending on the direction"""
		move = [0, 0]

		if directions[RIGHT]:
			move[0] += self.speed/10
		if directions[LEFT]:
			move[0] -= self.speed/10
		if directions[DOWN]:
			move[1] += self.speed/10
		if directions[UP]:
			move[1] -= self.speed/10

		move = tuple(move)

		if self.valid_movement(move):
			new_position = self.rect.move_ip(move) # Obtain position after movement
		else:
			self.life -= 1

	# ==========================================================================
	def valid_movement(self, coordenates):
		if self.collision_group:
			old_position = self.rect
			new_position = self.rect.move(coordenates)
			self.rect = new_position

			collision_list = pygame.sprite.spritecollide(self,
													self.collision_group, False)
			if len(collision_list) == 0:
				return True
			else:
				self.rect = old_position
				return False
		else:
			return True

	# ==========================================================================
	def process_collisions(self):
		pass

	# ==========================================================================
	def monitor_life(self):
		if self.life <= 0:
			self.die()

	# ==========================================================================
	def die(self):
		self.kill()

	# ==========================================================================
	def look(self, target):
		""" Update the sprite for the being to always face the cursor"""
		angle = geometry.angle_between(self.rect, target)

		if angle >= 45 and angle <= 135:
			direction = 'north'
		elif angle > 135 or angle < -135:
			direction = 'west'
		elif angle >= -135 and angle <= -45:
			direction = 'south'
		elif angle > -45 and angle < 45:
			direction = 'east'

		image_name = '%(sprite)s_%(direction)s' % {'sprite':self.sprite_prefix,
														'direction':direction}
		self.image, a = load_image(image_name, -1)

	# ==========================================================================
	def attack(self, weapon):
		""" Call the attack method of the default weapon"""

	# ==========================================================================
	def melee_attack(self):
		""" Attack with your own hands"""

