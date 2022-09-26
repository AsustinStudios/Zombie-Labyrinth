#!/usr/bin/env python3
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
E-mail: roberto@lapuente.me
Date: 2013-11-05
"""

import sys
from optparse import OptionParser

import pygame  # TODO: Replace import with just what we need
from pygame.constants import (
    K_a,
    K_d,
    K_DOWN,
    K_ESCAPE,
    K_F1,
    K_F2,
    K_LEFT,
    K_RIGHT,
    K_s,
    K_UP,
    K_w,
    KEYDOWN,
    MOUSEBUTTONDOWN,
    QUIT
)

from zombie_labyrinth.ai import look
from zombie_labyrinth.camera import follow_char
from zombie_labyrinth.engine import prepare_engine
from zombie_labyrinth.global_variables import allsprites, preferences
from zombie_labyrinth.input import get_directions
from zombie_labyrinth.levels import DEMO
from zombie_labyrinth.living_beings import TOPO
from zombie_labyrinth.resources import load_level


def main():
    process_cli_options()

    screen, background = prepare_engine('Zombie Attack!')
    load_level(DEMO, TOPO)

    status = main_loop(screen, background, look, follow_char)

    return status


def main_loop(screen, background, run_ai, camera_effect):
    font = pygame.font.Font(None, 20)
    hud = pygame.Surface((screen.get_size()[0], 20))
    clock = pygame.time.Clock()
    pygame.key.set_repeat(10, 20)

    while True:
        clock.tick(120)  # Set target FPS
        fps = clock.get_fps()

        # Loose condition
        if preferences.player.life <= 0:
            return 0

        # Handle Input Events
        for event in pygame.event.get():  # TODO: Get the input event control outside of the main loop
            if event.type == QUIT:
                return 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return 0
                elif event.key in (K_RIGHT, K_LEFT, K_UP, K_DOWN, K_d, K_a, K_w, K_s):
                    keys = pygame.key.get_pressed()
                    preferences.player.move(get_directions(keys))
                elif event.key == K_F1:
                    # Toggle FULL HD
                    if screen.get_size() == (1280, 720):
                        new_size = (1920, 1080)
                    elif screen.get_size() == (1920, 1080):
                        new_size = (1280, 720)
                    if screen.get_flags() & pygame.FULLSCREEN:
                        screen = pygame.display.set_mode(new_size, pygame.FULLSCREEN |
                                                         pygame.DOUBLEBUF | pygame.HWSURFACE)
                    else:
                        screen = pygame.display.set_mode(new_size, pygame.DOUBLEBUF)
                    background = pygame.Surface(screen.get_size())
                    background = background.convert()
                    background.fill((61, 61, 61))
                elif event.key == K_F2:
                    # Toggle Fullscreen
                    if screen.get_flags() & pygame.FULLSCREEN:
                        screen = pygame.display.set_mode(screen.get_size(), pygame.DOUBLEBUF)
                    else:
                        screen = pygame.display.set_mode(screen.get_size(), pygame.FULLSCREEN |
                                                         pygame.DOUBLEBUF | pygame.HWSURFACE)
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    preferences.player.attack(0)
                elif event.button == 3:
                    preferences.player.attack(1)

        pos = pygame.mouse.get_pos()    # TODO: Human Object must be bindable to
        preferences.player.look(pos)    # a device or a target must be specifyable.

        run_ai()

        # Mantener la cámara en el centro del nivel
        camera_effect(preferences.player)

        # Update all the sprites
        allsprites.update()

        # Display Current FPS (HUD)
        wp = (str(preferences.player.weapons[0]), str(preferences.player.weapons[1]))
        hud.fill((22, 22, 22))
        hud_text = (
            'F1: Toggle HD  |  F2: Toggle Fullscreen  |  ESC: Quit'
            '                                                     '
            f'FPS: {fps:4.0f} | Life: {preferences.player.life} | '
            f'Weapons: {wp} | Status: {preferences.player.status}'
        )

        text = font.render(hud_text, 1, (255, 255, 255))
        textpos = text.get_rect(x=5, y=3)
        hud.blit(text, textpos)

        # Draw the entire scene
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        screen.blit(hud, (0, 0))

        pygame.display.flip()

    # Game Over


def process_cli_options():
    """ Process the command line interface options and return a Preferences
    object"""
    parser = OptionParser(usage='Configuration options')
    parser.add_option('--height ', '-y',
                      dest='y',
                      type='int',
                      metavar='Height',
                      default="1080",
                      help='Window height')
    parser.add_option('--width', '-x',
                      dest='x',
                      type='int',
                      metavar='width',
                      default='1920',
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


if __name__ == '__main__':
    if not pygame.font:
        print('Warning, fonts disabled')
    if not pygame.mixer:
        print('Warning, sound disabled')
    sys.exit(main())
