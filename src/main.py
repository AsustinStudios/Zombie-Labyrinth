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

import sys
import pygame
import preferences
from pygame.locals import *
from optparse import OptionParser
import preferences

# ==============================================================================
def main():
	preferences = process_cli_options()
	status = main_loop()

	return status

# ==============================================================================
def main_loop():
	# Initialize Everything
	pygame.init()
	screen = pygame.display.set_mode((600, 400))
	pygame.display.set_caption('Zombie Labyrinth')
	pygame.mouse.set_visible(0)

	# Create Background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	# Display Background
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Prepare Game Objects
	punch_sound = load_sound('punch.wav')
	zombie = Zombie()
	human = Human()
	allsprites = pygame.sprite.RenderPlain((chimp, fist))
	clock = pygame.time.Clock()

	global score
	score = 0

	while True:
		clock.tick(60)

		# Handle Input Events
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return
			elif event.type == MOUSEBUTTONDOWN:
				if fist.punch(chimp):
					punch_sound.play() #punch
					chimp.punched()
				else:
					pass
					#whiff_sound.play() #miss
			elif event.type == MOUSEBUTTONUP:
				fist.unpunch()

		# Score
		if score != 0:
			background.fill((250, 250, 250))
			font = pygame.font.Font(None, 36)
			text = font.render("Pummel The Chimp! %i" % score, 1, (10, 10, 10))
			textpos = text.get_rect(centerx=background.get_width()/2)
			background.blit(text, textpos)

		# Update all the sprites
		allsprites.update()

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

	# Check for command line options
	if not (options.tabla and options.PWD and (options.encabezado or options.num_campos)) and (options.parsear and (options.tipo_archivo == None)):
		sys.exit(parser.error(rojo + 'Parametros incompletos'))

	# Assign options to preferences
	preferences = preferences.Preferences()

	return preferences

# ==============================================================================
if __name__ == '__main__':
	if not pygame.font: print 'Warning, fonts disabled'
	if not pygame.mixer: print 'Warning, sound disabled'
	sys.exit(main())
