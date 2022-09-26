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
import os

from pygame import error
from pygame import image
from pygame import mixer
from pygame.constants import RLEACCEL
from pygame.rect import Rect
from pygame.surface import Surface

from zombie_labyrinth.constants import Mode, Direction
from zombie_labyrinth.global_variables import allsprites, chars_objects_group, zombies_objects_group


def load_sprite(name, status=Mode.standard, direction=Direction.south, number=0, colorkey=None) -> tuple[Surface, Rect]:
    """ This Functions loads a png image and returns the image object and the image rect"""

    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    fullname = os.path.join(path, '../..', 'resources', 'sprites', name,
                            status.value, direction.value, f'{name}_{number:02}.png')
    try:
        sprite = image.load(fullname)
    except error as e:
        raise SystemExit(f'Cannot load image: {name}') from e
    sprite = sprite.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = sprite.get_at((0, 0))
        sprite.set_colorkey(colorkey, RLEACCEL)
    return sprite, sprite.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not mixer:
        return NoneSound()

    name = '%s.mp3' % name
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    fullname = os.path.join(path, '../..', 'resources', 'sounds', name)
    try:
        sound = mixer.Sound(fullname)
    except error as e:
        raise SystemExit(f'Cannot load sound: {fullname!r}') from e
    return sound


def load_song(name):
    mixer.init()

    class NoneSound:
        def play(self): pass
    if not mixer:
        return NoneSound()

    name = f'{name}.mp3'
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    fullname = os.path.join(path, '../..', 'resources', 'music', name)
    try:
        mixer.music.load(fullname)
    except error as e:
        raise SystemExit(f'Cannot load sound: {fullname!r}') from e


def play_song(loop=False, song=None):
    if song is not None:
        load_song(song)

    mixer.music.play(-1 if loop else 0)


def load_map(name):
    """ This Function loads all the level construction, create the objects and
    get them in their respective groups."""
    from zombie_labyrinth.game_objects import GameObject  # Avoid circular import

    name = '%s.lvl' % name
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    fullname = os.path.join(path, '../..', 'resources', 'levels', name)
    terrain_type = {'F': 'floor', 'W': 'wall'}

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
            pos = (j*64, i*64+20)  # The +20 is to account for the HUD space
            new_obj = GameObject(pos, terrain_type[type])
            new_obj.life = life
            allsprites.add(new_obj)
            if type == 'W':
                chars_objects_group.add(new_obj)
                zombies_objects_group.add(new_obj)
            j += 1
        line = file.readline()
        i += 1


def load_level(level, character):
    """ This Should load missions from a text file or have a function for each
    mission or level. However, for the time being it just loads the default map
    and settings."""
    from zombie_labyrinth.levels import load_demo, DEMO  # Avoid circular import

    if level == DEMO:
        load_demo(character)
    elif True:
        pass
    else:
        pass
