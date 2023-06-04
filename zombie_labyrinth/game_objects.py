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



from pygame.rect import Rect
from pygame.sprite import Sprite, spritecollide

from zombie_labyrinth.constants import Direction
from zombie_labyrinth.resources import load_sprite


class GameObject(Sprite):
    """The super class that represents all objects on the game on the game."""

    def __init__(self, location, object_type):
        super().__init__()
        self.image, self.rect = load_sprite(object_type)
        self.rect: Rect = self.rect.move(location)
        self.object_type = object_type
        self.life: int = 100
        self.direction = Direction.south
        self.animation_count = 0

    def update(self):
        """Update the Object."""
        pass

    def receive_damage(self, damage):
        """Receive damage, process it and apply it to life."""
        self.life -= damage


class Bullet(GameObject):
    """The super class that represents proyectiles in the game."""

    def __init__(self, start_location, direction, collision_group, speed=200, strength=10, object_type='bullet'):
        super().__init__(start_location, object_type)

        self.direction = direction
        self.image, _ = load_sprite(self.object_type, direction=self.direction)
        self.speed = self.get_coordinate_speed(direction, speed)
        self.collision_group = collision_group
        self.strength = strength

    def update(self):
        """Update the Object."""
        self.move()
        self.process_collisions()

    def process_collisions(self):
        collision_list = spritecollide(self, self.collision_group, False)
        if len(collision_list) != 0:
            self.kill()
            for obj in collision_list:
                obj.receive_damage(self.strength)

    def move(self):
        """Move around the being depending on the direction."""
        self.rect.move_ip(self.speed)

    def get_coordinate_speed(self, direction, speed):
        """Receives a speed and returns the (x,y) pair needed by `rect.move()` to move at the received speed."""
        x, y = 0, 0

        if direction == Direction.north:
            y = -speed/10
        elif direction == Direction.east:
            x = speed/10
        elif direction == Direction.south:
            y = speed/10
        elif direction == Direction.west:
            x = -speed/10

        return (x, y)
