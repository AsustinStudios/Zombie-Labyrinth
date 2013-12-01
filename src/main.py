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

import sys
from optparse import OptionParser

import pygame
from pygame.locals import *

import input
import preferences
import geometry
from global_variables import *
from human import Human
from zombie import Zombie
from game_object import Game_object
from weapons import *

# ==============================================================================
def main():
	preferences = process_cli_options()

	status = main_loop()

	return status

# ==============================================================================
def main_loop():
	# Initialize Everything
	pygame.init()
	screen = pygame.display.set_mode((1280, 720))
	pygame.display.set_caption('Zombie Labyrinth')
	pygame.mouse.set_visible(True)

	# Create Background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((205, 133, 63))

	# Text
	font = pygame.font.Font(None, 20)
	text = font.render("FPS:   | Life: ", 1, (10, 10, 10))
	textpos = text.get_rect(centerx=background.get_width()/2)
	background.blit(text, textpos)

	# Display Background
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Prepare Game Objects
	objects_group = pygame.sprite.Group()
	human = Human()
	human.weapons[0] = Cold_weapon(40, 50)
	human.weapons[1] = Firearm(40)
	human.collision_group = objects_group

	zombie = Zombie((400,400))
	objects_group.add(zombie)

	wall = Game_object((300,300), 'wall', 'WALL')
	objects_group.add(wall)

	allsprites.add(zombie, human, wall)
	clock = pygame.time.Clock()
	pygame.key.set_repeat(10, 20)

	while True:
		clock.tick(60)
		fps = clock.get_fps()

		# Handle Input Events
		for event in pygame.event.get():
			if event.type == QUIT:
				return 0
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					return 0
				elif event.key in (K_RIGHT, K_LEFT, K_UP, K_DOWN, K_d, K_a, K_w, K_s):
					keys = pygame.key.get_pressed()
					human.move(input.get_directions(keys))
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					human.attack(0)
				elif event.button == 3:
					human.attack(1)

		pos = pygame.mouse.get_pos()	# TODO: Human Object must be bindable to
		human.look(pos)					# a device or a target must be specifyable.

		# Mantener la cámara en el centro del nivel
		newpos = (human.rect[0], human.rect[1])
		distance = geometry.delta((600,300), newpos)
		if distance != (0,0):
			distance = (-distance[0], -distance[1])
			for spr in allsprites.sprites():
				spr.rect.move_ip(distance)

		# Update all the sprites
		allsprites.update()

		# Display Current FPS
		background.fill((205, 133, 63))
		text = font.render("FPS: %i | Life: %i" % (fps, human.life), 1, (10, 10, 10))
		textpos = text.get_rect(centerx=background.get_width()/2)
		background.blit(text, textpos)

		# Draw the entire scene
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		pygame.display.flip()

	# Game Over

# ==============================================================================
def process_cli_options():
	""" Process the command line interface options and return a Preferences
	object"""
	parser = OptionParser(usage='Ejecuta el proceso de ETL')
	parser.add_option('--directorio', '--dir', '-d',
					  dest='directorio',
					  metavar='Directorio',
					  default=".",
					  help='Directorio')
	parser.add_option('--patron', '-p',
					  dest='patron',
					  metavar='Patron',
					  default=".txt",
					  help='Patron')
	parser.add_option('--header',
					  dest='line_header',
					  action="store_true",
					  metavar='header',
					  default=False,
					  help='Si una función tiene o no un header')
	options, args = parser.parse_args()

	# Assign options to preferences
	preferencess = preferences.Preferences()

	return preferences

# ==============================================================================
if __name__ == '__main__':
	if not pygame.font: print 'Warning, fonts disabled'
	if not pygame.mixer: print 'Warning, sound disabled'
	sys.exit(main())
