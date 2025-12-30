"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: food.py
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


import pygame as pg
import random


class Food:
    def __init__(self, screen):
        self.pos = pg.math.Vector2(random.randint(0, screen.get_width()),
                                   random.randint(0, screen.get_height()))
        self.radius = 2.5
        self.screen = screen

    def render(self):
        pg.draw.ellipse(self.screen, 
                        (0, 255, 0), 
                        (self.pos.x, self.pos.y, self.radius*2, self.radius*2))
