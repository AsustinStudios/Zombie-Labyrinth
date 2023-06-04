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


from zombie_labyrinth.geometry import delta
from zombie_labyrinth.global_variables import allsprites, screen_center


def follow_char(character):
    """Make the camera follow the character.

    This function moves the camera so that it will always stay on top of the
    object given in the 'character' parameter. Usually used to follow the player
    but this is also useful when making in game cinematics during the campaing.
    """
    newpos = (character.rect[0], character.rect[1])
    distance = delta(screen_center, newpos)
    if distance != (0, 0):
        distance = (-distance[0], -distance[1])
        for spr in allsprites.sprites():
            spr.rect.move_ip(distance)


def fancy_new_cam(character):
    """Make the camera follow the character.

    Similar to the 'follow_char' but this camera should work like the cam in
    'Zelda: Minish Cap' when you reach the end of a room, the camera stays still
    and the    char gets to move all the way to the end of the screen.
    """
    pass
