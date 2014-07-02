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

This file contains the preferences of the current execution and global game
preferences.
"""

# ==============================================================================
class Preferences():
	""" This class manages the global and current execution game preferences."""
	def __init__(self):
		self.player = None
		self.size = (1920, 1080)
		self.fullscreen = True
