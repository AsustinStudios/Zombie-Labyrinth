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
Date: 2014-03-06
"""

import pygame

from src.global_variables import preferences

# ==============================================================================
def prepare_engine(window_title=''):
    # Initialize the engine, screen && background
    pygame.init()
    pygame.display.set_caption(window_title)
    pygame.mouse.set_visible(True)

    # Play intro video
    #movieplayer.main('/home/roberto/Videos/Banned Commercials - Microsoft Office XP (Banned Too Sexy).mpeg')

    # Initialize screen && drawing area
    if preferences.fullscreen:
        flags = pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE
    else:
        flags = pygame.DOUBLEBUF

    screen = pygame.display.set_mode(preferences.size, flags)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((61, 61, 61))

    return screen, background
