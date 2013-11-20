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

import geometry
from input import *
from resources import *
from abstract_game_objects import Game_object

# ==============================================================================
global RIGHT, LEFT, NORTH, SOUTH, EAST, WEST

RIGHT = 0
LEFT = 1
NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'

# ==============================================================================
class Living_being(Game_object):
	""" The class that represents all the living entities in the game"""

	# ==========================================================================
	def __init__(self, start_location=(50, 50), sprite_prefix='living_being', object_type='LIVING'):
		Game_object.__init__(self, start_location, sprite_prefix, object_type)
		self.collision_group = None
		self.direction = NORTH

		# ======================================================================
		""" Permanent Stats"""
		self.handedness = 0
		self.melee_range = 10
		self.life = 100

		""" Trainable Stats"""
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

		# Adjust direction Sprite
		image_name = '%(sprite)s_%(direction)s' % {'sprite':self.sprite_prefix,
													'direction':self.direction}
		self.image, a = load_image(image_name, -1)

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
			pass

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
			self.direction = NORTH
		elif angle > 135 or angle < -135:
			self.direction = WEST
		elif angle >= -135 and angle <= -45:
			self.direction = SOUTH
		elif angle > -45 and angle < 45:
			self.direction = EAST

	# ==========================================================================
	def attack(self, weapon):
		""" Call the attack method of the default weapon"""
		if not weapon:
			melee_attack()

	# ==========================================================================
	def melee_attack(self):
		""" Attack with your own hands"""
		if self.collision_group:
			sprite_position = self.rect
			melee_rect = create_melee_rect()
			self.rect = melee_rect

			collision_list = pygame.sprite.spritecollide(self,
													self.collision_group, False)
			self.rect = sprite_position
			for sprite in collision_list:
				sprite.receive_damage(self.strength)

	# ==========================================================================
	def create_melee_rect(self):
		""" Create a new rect object that represents the range in which you can
		do melee damage"""
		# Original Values
		original_x = self.rect[0]
		original_y = self.rect[1]
		original_width = self.rect[2]
		original_height = self.rect[3]

		# Melee Rect Values Adjusted to char Rotation
		if self.direction == NORTH:
			if self.handedness == RIGHT:
				x = original_x + (original_width/2)
				y = original_y - self.melee_range
				width = original_width/2
				height = self.melee_range
			elif self.handedness == LEFT:
				x = original_x
				y = original_y - self.melee_range
				width = original_width/2
				height = self.melee_range
		elif self.direction == EAST:
			if self.handedness == RIGHT:
				x = original_x + original_width + self.melee_range
				y = original_y + original_height/2
				width = self.melee_range
				height = original_height/2
			elif self.handedness == LEFT:
				x = original_x + original_width + self.melee_range
				y = original_y
				width = self.melee_range
				height = original_height/2
		elif self.direction == SOUTH:
			if self.handedness == RIGHT:
				x = original_x
				y = original_y + original_height + self.melee_range
				width = original_width/2
				height = self.melee_range
			elif self.handedness == LEFT:
				x = original_x + (original_width/2)
				y = original_y + original_height + self.melee_range
				width = original_width/2
				height = self.melee_range
		elif self.direction == WEST:
			if self.handedness == RIGHT:
				x = original_x - self.melee_range
				y = original_y
				width = self.melee_range
				height = original_height/2
			elif self.handedness == LEFT:
				x = original_x - self.melee_range
				y = original_y + original_height/2
				width = self.melee_range
				height = original_height/2

		return pygame.Rect(x, y, width, height)

	# ==========================================================================
	def receive_damage(self, damage):
		""" Receive damage, process it and apply it to life"""
		pass
