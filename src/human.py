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
import geometry
from pygame.locals import *
from resources import *

# ==============================================================================
class Human(pygame.sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # call Sprite initializer
		self.image, self.rect = load_image('human.png', -1)
		self.punching = 0
		self.speed = 3

		self.rect = self.rect.move((200, 200))

	def update(self):
		pass

	def move(self, keys):
		move = [0, 0]
		keys = pygame.key.get_pressed()

		if keys[K_d] or keys[K_RIGHT]:
			move[0] += self.speed
		if keys[K_a] or keys[K_LEFT]:
			move[0] -= self.speed
		if keys[K_s] or keys[K_DOWN]:
			move[1] += self.speed
		if keys[K_w] or keys[K_UP]:
			move[1] -= self.speed

		move = tuple(move)
		newpos = self.rect.move(move)
		self.rect = newpos

	def update_res(self):
		"move the fist based on the mouse position"

		self.rect.midtop = pos
		if self.punching:
			self.rect.move_ip(5, 10)

	def punch(self, target):
		"returns true if the fist collides with the target"
		if not self.punching:
			self.punching = 1
			hitbox = self.rect.inflate(-5, -5)
			return hitbox.colliderect(target.rect)

	def unpunch(self):
		"called to pull the fist back"
		self.punching = 0

	def look(self, target):
		print self.rect, target
		print geometry.delta(self.rect, target)
		print geometry.angle_between(self.rect, target)
		angle = geometry.angle_between(self.rect, target)
		if angle >= 45 and angle <= 135:
			self.image, a = load_image('human_north.png', -1)
		elif angle > 135 or angle < -135:
			self.image, a = load_image('human_west.png', -1)
		elif angle >= -135 and angle <= -45:
			self.image, a = load_image('human_south.png', -1)
		elif angle > -45 and angle < 45:
			self.image, a = load_image('human_east.png', -1)
