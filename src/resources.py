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
Date: 2013-11-05
"""

import sys, os

import pygame
from pygame.locals import *

from global_variables import *
from game_object import Game_object

# ==============================================================================
def load_image(name, colorkey=None):
	""" This Functions loads a png image and returns the image object and the
	image rect"""
	name = '%s.png' % name
	path = os.path.dirname(os.path.abspath(sys.argv[0]))
	fullname = os.path.join(path, '..', 'resources', 'images', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', name
		raise SystemExit, message
	image = image.convert()
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image, image.get_rect()

# ==============================================================================
def load_sound(name):
	class NoneSound:
		def play(self): pass
	if not pygame.mixer:
		return NoneSound()
	path = os.path.dirname(os.path.abspath(sys.argv[0]))
	fullname = os.path.join(path, '..', 'data', 'sounds', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print 'Cannot load sound:', wav
		raise SystemExit, message
	return sound

# ==============================================================================
def load_level(name):
	""" This Function loads all the level construction, create the objects and
	get them in their respective groups."""
	name = '%s.lvl' % name
	path = os.path.dirname(os.path.abspath(sys.argv[0]))
	fullname = os.path.join(path, '..', 'resources', 'levels', name)
	terrain_type = {	'F':'floor',
						'W':'wall'}

	file = open(fullname, 'r')
	line = file.readline()
	i = 0

	while line:
		list = line.strip('\n').split('|')
		j = 0
		for elem in list:
			elem = elem.split(':')
			type = elem[0]
			life = int(elem[1])
			pos = (j*64, i*64+20)
			new_obj = Game_object(pos, terrain_type[type])
			new_obj.life = life
			allsprites.add(new_obj)
			if type == 'W':
				objects_group.add(new_obj)
			j += 1
		line = file.readline()
		i += 1
