"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                      Program Name: Cellular-Evolution
                Description: Simulation of cellular evolution.
                                File: main.py
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


import world


class Main:
    def __init__(self):
        self.world = world.World()
        

if __name__ == '__main__':
    main = Main()

    main.world.execute()
