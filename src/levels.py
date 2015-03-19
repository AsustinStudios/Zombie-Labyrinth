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

import living_beings
import resources
import weapons

from global_variables import allsprites, objects_group, preferences

# ==============================================================================
global DEMO
""" Global constants defining all the possible levels of the game. Each constant
should have a corresponding function that loads that level."""
DEMO = 0

# ==============================================================================
def load_demo(character):
	""" Load the map and starting settings for the game demo."""
	resources.load_map('demo')
	resources.play_song(True, 'lluvia')

	character = living_beings.new_human((2000,2000), character)
	powerup = living_beings.new_human((1500,1500))

	interact_group = pygame.sprite.Group()
	interact_group.add(powerup)
	character.interact_group = interact_group

	zombies = (living_beings.new_zombie((400,400)), living_beings.new_zombie((200,200)),
			living_beings.new_zombie((600,600)), living_beings.new_zombie((600,400)),
			living_beings.new_zombie((600,200)), living_beings.new_zombie((900,300)))
	objects_group.add(zombies)

	allsprites.add(zombies, powerup, character)

	preferences.player = character
