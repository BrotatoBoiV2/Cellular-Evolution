"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: food.py
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

import pygame as pg
import random

class Food:
    def __init__(self, screen):
        self.pos = pg.math.Vector2(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))
        self.radius = 2.5
        self.screen = screen

    def render(self):
        pg.draw.ellipse(self.screen, (0, 255, 0), (self.pos.x, self.pos.y, self.radius*2, self.radius*2))
