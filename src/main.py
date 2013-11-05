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

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# ==============================================================================
def main():
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
	chimp = Chimp()
	fist = Fist()
	allsprites = pygame.sprite.RenderPlain((chimp, fist))
	clock = pygame.time.Clock()

	global score
	score = 0

	# Main Loops
	while True:
		clock.tick(60)

		#Handle Input Events
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

		#Draw the entire scene
		screen.blit(background, (0, 0))
		allsprites.draw(screen)
		pygame.display.flip()

	#Game Over

# ==============================================================================
def load_image(name, colorkey=None):
	fullname = os.path.join('data', name)
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
	fullname = os.path.join('data', name)
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error, message:
		print 'Cannot load sound:', wav
		raise SystemExit, message
	return sound

# ==============================================================================
class Fist(pygame.sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #call Sprite initializer
		self.image, self.rect = load_image('hand.png', -1)
		self.punching = 0

	def update(self):
		"move the fist based on the mouse position"
		pos = pygame.mouse.get_pos()
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

# ==============================================================================
class Chimp(pygame.sprite.Sprite):
	"""moves a monkey critter across the screen. it can spin the
	   monkey when it is punched."""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #call Sprite intializer
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

# ==============================================================================
if __name__ == '__main__':
    import sys
    from optparse import OptionParser
    sys.exit(main())
