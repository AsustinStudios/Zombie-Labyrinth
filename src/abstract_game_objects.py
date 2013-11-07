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

# ==============================================================================
class Game_object(pygame.sprite.Sprite):
	""" The class that represents the human player on the game"""
	def __init__(self, location, sprite_prefix):
		pygame.sprite.Sprite.__init__(self) # call Sprite initializer
		self.image, self.rect = load_image(sprite_prefix, -1)
		self.sprite_prefix = sprite_prefix
		self.rect = self.rect.move(location)

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		pass

# ==============================================================================
class Living_being(Game_object):
	""" The class that represents all the living entities in the game"""
	def __init__(self, start_location, sprite_prefix='living_being', speed=3):
		Game_object.__init__(self, start_location, sprite_prefix)
		self.speed = speed

	# ==========================================================================
	def update(self):
		""" Update the Object"""
		pass

	# ==========================================================================
	def move(self, directions, collision_group=None):
		""" Move around the being depending on the direction"""
		move = [0, 0]

		if directions[RIGHT]:
			move[0] += self.speed
		if directions[LEFT]:
			move[0] -= self.speed
		if directions[DOWN]:
			move[1] += self.speed
		if directions[UP]:
			move[1] -= self.speed

		move = tuple(move)
		newpos = self.rect.move_ip(move)

		if collision_group:
			collision_list = pygame.sprite.spritecollide(self, collision_group, False)
			for object in collision_list:
				print object.rect



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

		image_name = '%(sprite)s_%(direction)s' % {'sprite':self.sprite_prefix, 'direction':direction}
		self.image, a = load_image(image_name, -1)
