"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: world.py
                              Date: 2025/12/04
                          Version: 0.3-2025.12.05

===============================================================================

                        Copyright (C) 2025 BrotatoBoi
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published
        by: The Free Software Foundation, either the version 3 of the
        License, or any later version.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import cells
import random
import time
import pygame as pg


class World:
    def __init__(self):
        self.size = (800, 600)
        self.screen = pg.display.set_mode(self.size)
        self.cells = []

        # for _ in range(3):
        #     pos = pg.math.Vector2(random.randint(0, self.size[0]), random.randint(0, self.size[1]))

        #     self.cells.append(cells.Cell(pos.x, pos.y, self.screen))

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                print("Creating cell")
                self.cells.append(cells.Cell(pos[0], pos[1], self.screen))
                

    def render(self):
        self.screen.fill((0, 0, 0))

        for cell in self.cells:
            cell.render()


    def update(self):
        new_cells = []
        for cell in self.cells:
            cell.update()

            if cell.energy <= 0.0:
                continue
                
            new_cells.append(cell)

        self.cells = new_cells


        pg.display.update()
