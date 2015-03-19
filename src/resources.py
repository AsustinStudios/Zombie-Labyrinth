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

import game_objects
import levels

from global_variables import allsprites, chars_objects_group, zombies_objects_group, preferences, SOUTH, STANDARD

# ==============================================================================
def load_sprite(name, status=None, direction=None, number=0, colorkey=None):
	""" This Functions loads a png image and returns the image object and the
	image rect"""
	if direction == None:
		direction = SOUTH
	if status == None:
		status = STANDARD

	path = os.path.dirname(os.path.abspath(sys.argv[0]))
	fullname = os.path.join(path, '..', 'resources', 'sprites', name, status,
							direction, '%s_%02d.png' % (name, number))
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', name
		raise SystemExit, message
	image = image.convert_alpha()
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

	name = '%s.mp3' % name
	path = os.path.dirname(os.path.abspath(sys.argv[0]))
	fullname = os.path.join(path, '..', 'resources', 'sounds', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print 'Cannot load sound:', wav
		raise SystemExit, message
	return sound

# ==============================================================================
def load_song(name):
	pygame.mixer.init()
	class NoneSound:
		def play(self): pass
	if not pygame.mixer:
		return NoneSound()

	name = '%s.mp3' % name
	path = os.path.dirname(os.path.abspath(sys.argv[0]))
	fullname = os.path.join(path, '..', 'resources', 'music', name)
	try:
		pygame.mixer.music.load(fullname)
	except pygame.error, message:
		print 'Cannot load sound:', wav
		raise SystemExit, message

# ==============================================================================
def play_song(loop=False, song=None):
	if song != None:
		load_song(song)

	pygame.mixer.music.play(-1 if loop else 0)

# ==============================================================================
def load_map(name):
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
			pos = (j*64, i*64+20) # The +20 is to account for the HUD space
			new_obj = game_objects.Game_object(pos, terrain_type[type])
			new_obj.life = life
			allsprites.add(new_obj)
			if type == 'W':
				chars_objects_group.add(new_obj)
				zombies_objects_group.add(new_obj)
			j += 1
		line = file.readline()
		i += 1

# ==============================================================================
def load_level(level, character):
	""" This Should load missions from a text file or have a function for each
	mission or level. However, for the time being it just loads the default map
	and settings."""
	if level == levels.DEMO:
		levels.load_demo(character)
	elif True:
		pass
	else:
		pass
