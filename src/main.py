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

from global_variables import *
import resources
import input
import geometry
import camera
import ai
import engine

from human import Human
from zombie import Zombie
from game_object import Game_object
from weapons import *

# ==============================================================================
def main():
	process_cli_options()

	screen, background = engine.prepare_engine('Zombie Attack!')
	resources.load_level('demo')

	status = main_loop(screen, background, ai.main_ai, camera.follow_char)

	return status

# ==============================================================================
def main_loop(screen, background, run_ai, camera_effect):
	font = pygame.font.Font(None, 20)

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
					preferences.player.move(input.get_directions(keys))
				elif event.key == K_F1:
					screen = pygame.display.set_mode((1280, 720))
				elif event.key == K_F2:
					screen = pygame.display.set_mode((1280, 720),pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					preferences.player.attack(0)
				elif event.button == 3:
					preferences.player.attack(1)

		pos = pygame.mouse.get_pos()	# TODO: Human Object must be bindable to
		preferences.player.look(pos)	# a device or a target must be specifyable.

		run_ai()

		# Mantener la cámara en el centro del nivel
		camera_effect(preferences.player)

		# Update all the sprites
		allsprites.update()

		# Display Current FPS
		hud = pygame.Surface((screen.get_size()[0],20))
		hud.fill((22, 22, 22, 255))
		text = font.render('FPS: %i | Life: %i' % (fps, preferences.player.life), 1, (255,255,255))
		textpos = text.get_rect(centerx=background.get_width()/2)
		hud.blit(text, textpos)

		# Draw the entire scene
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		screen.blit(hud, (0, 0))


		pygame.display.flip()

	# Game Over

# ==============================================================================
def process_cli_options():
	""" Process the command line interface options and return a Preferences
	object"""
	parser = OptionParser(usage='Configuration options')
	parser.add_option('--height ', '-y',
					  dest='y',
					  type='int',
					  metavar='Height',
					  default="720",
					  help='Window height')
	parser.add_option('--width', '-x',
					  dest='x',
					  type='int',
					  metavar='width',
					  default='1280',
					  help='Window wdth')
	parser.add_option('--fullscreen', '-f',
					  dest='fullscreen',
					  action="store_true",
					  metavar='Fullscreen',
					  default=False,
					  help='Weather or not window should start on fullscreen mode.')
	options, args = parser.parse_args()

	# Assign options to preferences
	preferences.size = (options.x, options.y)
	preferences.fullscreen = options.fullscreen

# ==============================================================================
if __name__ == '__main__':
	if not pygame.font: print 'Warning, fonts disabled'
	if not pygame.mixer: print 'Warning, sound disabled'
	sys.exit(main())
