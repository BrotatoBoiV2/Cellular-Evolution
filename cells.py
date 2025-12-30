"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: cells.py
                              Date: 2025/12/04
                          Version: 0.6-2025.12.09

===============================================================================

                        Copyright (C) 2025 BrotatoBoi
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU Affero General Public License as published
        by the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU Affero General Public License for more details.

        You should have received a copy of the GNU Affero General Public License
        along with this program. If not, see <https://www.gnu.org/licenses/>

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


import random
import noise

import pygame as pg


class Cell:
    def __init__(self, x, y, screen, energy=100.0):
        self.screen = screen
        self.color = (255, 0, 0)
        self.radius = 10
        self.pos = pg.math.Vector2(x, y)
        self.vel = pg.math.Vector2(random.uniform(-10, 10),
                                    random.uniform(-10, 10))
        self.acc = pg.math.Vector2(0, 0)
        self.max_speed = 180
        self.max_force = 600
        self.energy = energy
        self.noise_time_x = random.uniform(0, 1000)
        self.noise_time_y = random.uniform(0, 1000)

    def render(self):
        pg.draw.ellipse(self.screen, 
                        self.color, 
                        (self.pos.x-self.radius, self.pos.y-self.radius,
                            self.radius*2, self.radius*2))

    def check_split(self, world):
        if self.energy >= 120.00:
            energy = self.energy//2
            world.cells.append(Cell(self.pos.x, self.pos.y, 
                                    self.screen, energy))
            self.energy = energy

    def check_predators(self):
        mouse_pos = pg.math.Vector2(pg.mouse.get_pos())
        flee_vector = self.pos - mouse_pos
        distance_to_mouse = flee_vector.length()

        if distance_to_mouse < 150:
            if distance_to_mouse > 0:
                flee_vector.normalize_ip()

                flee_vector *= 500
                self.acc += flee_vector

    def move_cell(self, dt):
        self.pos += self.vel * dt

        if self.pos.x > self.screen.get_width() + self.radius:
            self.pos.x = -self.radius
        if self.pos.x < -self.radius:
            self.pos.x = self.screen.get_width() + self.radius
        if self.pos.y > self.screen.get_height() + self.radius:
            self.pos.y = -self.radius
        if self.pos.y < -self.radius:
            self.pos.y = self.screen.get_height() + self.radius

    def update(self, world, dt):
        self.acc = pg.math.Vector2(0, 0)
        noise_speed = 0.5
        self.noise_time_x += noise_speed * dt
        self.noise_time_y += noise_speed * dt

        noise_x = noise.pnoise1(self.noise_time_x)
        noise_y = noise.pnoise1(self.noise_time_y)

        random_force = pg.math.Vector2(noise_x, noise_y)
        if random_force.length() > 0:
            random_force.scale_to_length(self.max_force)

        self.acc += random_force

        self.check_predators()

        self.vel += self.acc * dt

        if self.vel.length() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)

        self.move_cell(dt)
        self.check_split(world)

        self.energy -= 0.1
