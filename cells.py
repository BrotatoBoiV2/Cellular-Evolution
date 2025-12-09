"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: cells.py
                              Date: 2025/12/04
                          Version: 0.4-2025.12.06

===============================================================================

                        Copyright (C) 2025 BrotatoBoi
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published
        by: The Free Software Foundation, either the version 3 of the
        License, or any later version.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


import random

import pygame as pg


class Cell:
    def __init__(self, x, y, screen, energy=100.0):
        self.screen = screen
        self.color = (255, 0, 0)
        self.radius = 10
        self.pos = pg.math.Vector2(x, y)
        self.vel = pg.math.Vector2(random.uniform(-10, 10), random.uniform(-10, 10))
        self.acc = pg.math.Vector2(0, 0)
        self.max_speed = 180
        self.max_force = 600
        self.energy = energy

    def render(self):
        pg.draw.ellipse(self.screen, self.color, (self.pos.x, self.pos.y, self.radius*2, self.radius*2))

    def check_food(self, world):
        new_foods = []

        for food in world.food:
            dx = food.pos.x - self.pos.x
            dy = food.pos.y - self.pos.y
            d2 = (dx*dx) + (dy*dy)
            r2 = self.radius * self.radius

            if d2 <= r2:
                self.energy += 25
                continue
                
            new_foods.append(food)

        world.food = new_foods

    def check_split(self, world):
        if self.energy >= 120.00:
            energy = self.energy//2
            world.cells.append(Cell(self.pos.x, self.pos.y, self.screen, energy))
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

        if self.pos.x > self.screen.get_width() + self.radius: self.pos.x = -self.radius
        if self.pos.x < -self.radius: self.pos.x = self.screen.get_width() + self.radius
        if self.pos.y > self.screen.get_height() + self.radius: self.pos.y = -self.radius
        if self.pos.y < -self.radius: self.pos.y = self.screen.get_height() + self.radius

    def update(self, world, dt):
        random_force = pg.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if random_force.length() > 0:
            random_force.scale_to_length(self.max_force)

        self.acc = random_force

        self.check_predators()

        self.vel += self.acc * dt

        if self.vel.length() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)

        self.move_cell(dt)
        self.check_food(world)
        self.check_split(world)

        self.energy -= 0.1
