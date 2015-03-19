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

import game_objects
import geometry
import global_variables
import resources
import weapons

from global_variables import RIGHT, LEFT, UP, DOWN, NORTH, SOUTH, EAST, WEST

# ==============================================================================
global GENERIC, ABIGAIL, DEXTER, NANO, TOPO
GENERIC = 0
ABIGAIL = 1
DEXTER = 2
NANO = 3
TOPO = 4
ZOMBIE = 5

# ==============================================================================
class Living_being(game_objects.Game_object):
	""" The class that represents all the living entities in the game"""

	# ==========================================================================
	def __init__(self, start_location=(50, 50), object_type='living_being'):
		game_objects.Game_object.__init__(self, start_location, object_type)
		self.collision_group = None
		self.interact_group = None
		self.status = None

		# ======================================================================
		""" Permanent Stats"""
		self.handedness = 0
		self.melee_range = 10
		self.life = 100

		""" Trainable Stats"""
		self.speed = 10
		self.strength = 10
		self.programming = 0
		self.data_sciencing = 0

		# ======================================================================
		""" Inventory"""
		self.weapons = [None, None]
		self.inventory = []

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		self.process_collisions()
		self.monitor_life()

		# Adjust direction Sprite && animation frame
		if self.animation_count >= 15:
			self.animation_count = 0
		if self.animation_count < 5:
			n = 0
		elif self.animation_count >= 10:
			n = 2
		else:
			n = 1
		self.image, a = resources.load_sprite(self.object_type, None,
												self.direction, n)

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
			self.animation_count += 1
		else:
			pass

	# ==========================================================================
	def valid_movement(self, coordenates):
		if not self.collision_group:
			return True

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

	# ==========================================================================
	def process_collisions(self):
		""" This method should detectd when the agent is standing in some
		terrain that affects it stats, weapons and items that can be picked up
		or powerups that modify the agents stats. """
		if not self.interact_group:
			self.status = ''
			return

		collision_list = pygame.sprite.spritecollide(self, self.interact_group, False)
		self.status = ''

		for element in collision_list:	# TODO: Finish this
			if element.object_type == 'weapon':
				pass
			elif element.object_type == 'powerup':
				pass
			elif element.object_type == 'terrain':
				pass
			self.status = element


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
			new_direction = NORTH
		elif angle > 135 or angle < -135:
			new_direction = WEST
		elif angle >= -135 and angle <= -45:
			new_direction = SOUTH
		elif angle > -45 and angle < 45:
			new_direction = EAST

		if new_direction != self.direction:
			self.animation_count = 0
			self.direction = new_direction

	# ==========================================================================
	def attack(self, current_weapon=0):
		""" Call the attack method of the default weapon"""
		weapon = self.weapons[current_weapon]

		if weapon == None:
			self.melee_attack(self.strength, self.melee_range)
		elif weapon.type == weapons.COLD_WEAPON:
			self.melee_attack(weapon.strength, weapon.range)
		elif weapon.type == weapons.FIREARM:
			weapon.attack(self.rect, self.direction, self.collision_group)

	# ==========================================================================
	def melee_attack(self, strength, range):
		""" Attack with your own hands"""
		if self.collision_group:
			sprite_position = self.rect
			melee_rect = self.create_melee_rect(range)
			self.rect = melee_rect

			collision_list = pygame.sprite.spritecollide(self,
													self.collision_group, False)
			self.rect = sprite_position
			for enemy in collision_list:
				enemy.receive_damage(strength)

	# ==========================================================================
	def create_melee_rect(self, range):
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
				y = original_y - range
				width = original_width/2
				height = range
			elif self.handedness == LEFT:
				x = original_x
				y = original_y - range
				width = original_width/2
				height = range
		elif self.direction == EAST:
			if self.handedness == RIGHT:
				x = original_x + original_width + range
				y = original_y + original_height/2
				width = range
				height = original_height/2
			elif self.handedness == LEFT:
				x = original_x + original_width + range
				y = original_y
				width = range
				height = original_height/2
		elif self.direction == SOUTH:
			if self.handedness == RIGHT:
				x = original_x
				y = original_y + original_height + range
				width = original_width/2
				height = range
			elif self.handedness == LEFT:
				x = original_x + (original_width/2)
				y = original_y + original_height + range
				width = original_width/2
				height = range
		elif self.direction == WEST:
			if self.handedness == RIGHT:
				x = original_x - range
				y = original_y
				width = range
				height = original_height/2
			elif self.handedness == LEFT:
				x = original_x - range
				y = original_y + original_height/2
				width = range
				height = original_height/2

		return pygame.Rect(x, y, width, height)

# ==============================================================================
def new_human(start_location=global_variables.screen_center, type=GENERIC):
	""" This function returns Human corresponding to some character. It should
	load that character base stats & stuff. Weapons, powerups and other stuff
	that are mission specific should be setup at the level."""
	human = Living_being(start_location, 'human')

	""" Permanent Stats"""
	human.handedness = 0
	human.melee_range = 10
	human.life = 100

	""" Trainable Stats"""
	human.speed = 20
	human.strength = 20
	human.programming = 15
	human.data_sciencing = 15

	if type == TOPO:
		human.object_type = 'topo'
		human.weapons[0] = weapons.Cold_weapon(40, 50, 'Knife')
		human.weapons[1] = weapons.Firearm(40, 'AK-47')
		human.collision_group = global_variables.objects_group
	elif type == NANO:
		human.object_type = 'nano'
		human.weapons[0] = weapons.Cold_weapon(40, 50, 'Knife')
		human.weapons[1] = weapons.Firearm(40, 'AK-47')
		human.collision_group = global_variables.objects_group
	elif type == DEXTER:
		human.object_type = 'dexter'
		human.weapons[0] = weapons.Cold_weapon(40, 50, 'Knife')
		human.weapons[1] = weapons.Firearm(40, 'AK-47')
		human.collision_group = global_variables.objects_group
	elif type == ABIGAIL:
		human.object_type = 'abigail'
		human.weapons[0] = weapons.Cold_weapon(40, 50, 'Knife')
		human.weapons[1] = weapons.Firearm(40, 'AK-47')
		human.collision_group = global_variables.objects_group
	return human

def new_zombie(start_location=global_variables.screen_center, type=ZOMBIE):
	""" This function returns Human corresponding to some character. It should
	load that character base stats & stuff. Weapons, powerups and other stuff
	that are mission specific should be setup at the level."""
	zombie = Living_being(start_location, 'zombie')

	""" Permanent Stats"""
	zombie.handedness = 0
	zombie.melee_range = 10
	zombie.life = 50

	""" Trainable Stats"""
	zombie.speed = 10
	zombie.strength = 10
	zombie.programming = 0
	zombie.data_sciencing = 0

	if type == ZOMBIE:
		zombie.object_type = 'zombie'
		zombie.weapons[0] = weapons.Cold_weapon(40, 50, 'Knife')
		zombie.weapons[1] = weapons.Firearm(40, 'AK-47')
		zombie.collision_group = global_variables.objects_group

	return zombie
