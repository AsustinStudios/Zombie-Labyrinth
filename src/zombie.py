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

import os, sys
import pygame
from pygame.locals import *

# ==============================================================================
class Zombie(pygame.sprite.Sprite):
	"""moves a monkey critter across the screen. it can spin the
	   monkey when it is punched."""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # Call Sprite intializer
		self.image, self.rect = load_image('chimp.png', -1)
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.rect.topleft = 10, 10
		self.l_move = 1
		self.r_move = 1
		self.dizzy = 0

	def update(self):
		"walk or spin, depending on the monkeys state"
		if self.dizzy:
			self._spin()
		else:
			self._walk()

	def _walk(self):
		"move the monkey across the screen, and turn at the ends"
		newpos = self.rect.move((self.l_move, self.r_move))
		if not self.area.contains(newpos):
			if self.rect.left < self.area.left or self.rect.right > self.area.right:
				self.l_move = -self.l_move
			if self.rect.top < self.area.top or self.rect.bottom > self.area.bottom:
				self.r_move = -self.r_move
			newpos = self.rect.move((self.l_move, self.r_move))
			self.image = pygame.transform.flip(self.image, 1, 0)
		self.rect = newpos

	def _spin(self):
		"spin the monkey image"
		center = self.rect.center
		self.dizzy += 12
		if self.dizzy >= 360:
			self.dizzy = 0
			self.image = self.original
		else:
			rotate = pygame.transform.rotate
			self.image = rotate(self.original, self.dizzy)
		self.rect = self.image.get_rect(center=center)

	def punched(self):
		"this will cause the monkey to start spinning"
		global score

		if not self.dizzy:
			score += 1
			self.l_move += 1
			self.r_move += 1
			self.dizzy = 1
			self.original = self.image
			self.l_move = -self.l_move
