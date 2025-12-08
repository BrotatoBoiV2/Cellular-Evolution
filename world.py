"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: world.py
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

import cells
import food
import random
import time
import pygame as pg


class World:
    def __init__(self):
        self.size = (800, 600)
        self.screen = pg.display.set_mode(self.size)
        self.cells = []
        self.food = []
        self.spawn_interval = 3.0
        self.last_time = 0.0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                self.cells.append(cells.Cell(pos[0], pos[1], self.screen))
                

    def render(self):
        self.screen.fill((0, 0, 0))

        for cell in self.cells:
            cell.render()

        for food in self.food:
            food.render()


    def spawn_food(self):
        dt = 0.5 / 240.0
        self.last_time += dt

        if self.last_time >= self.spawn_interval:
            self.food.append(food.Food(self.screen))
            self.last_time -= self.spawn_interval

    def update(self):
        new_cells = []
        
        for cell in self.cells:
            cell.update(self)

            if cell.energy <= 0.0:
                continue
                
            new_cells.append(cell)


        self.cells = new_cells

        self.spawn_food()

        pg.display.update()
