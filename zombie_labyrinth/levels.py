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

from pygame.sprite import Group

from zombie_labyrinth.global_variables import allsprites, chars_objects_group, zombies_objects_group, preferences
from zombie_labyrinth.living_beings import new_human, new_zombie


global DEMO
""" Global constants defining all the possible levels of the game. Each constant
should have a corresponding function that loads that level."""
DEMO = 0


def load_demo(character):
    """ Load the map and starting settings for the game demo."""
    from zombie_labyrinth.resources import load_map, play_song  # Avoid circular import

    load_map('demo')
    play_song(True, 'lluvia')

    character = new_human((96, 90), character)
    powerup = new_human((100, 750))

    interact_group = Group()
    interact_group.add(powerup)
    character.interact_group = interact_group

    zombies = (new_zombie((300, 400)), new_zombie((900, 600)),
               new_zombie((600, 600)), new_zombie((600, 400)),
               new_zombie((650, 500)), new_zombie((900, 300)))
    chars_objects_group.add(zombies)
    zombies_objects_group.add(zombies, character)

    allsprites.add(zombies, powerup, character)

    preferences.player = character
