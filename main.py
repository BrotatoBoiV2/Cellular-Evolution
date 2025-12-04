"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Programmer: Aaron "A.J." Cassell. (@BrotatoBoi)
                        Program Name: Cellular-Evolution
                 Description: Simulation of cellular evolution.
                              File: main.py
                            Date: 2025/12/04
                         Version: 0.1-2025.12.04

===============================================================================

                        Copyright (C) 2025 BrotatoBoi
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published
        by: The Free Software Foundation, either the version 3 of the
        License, or any later version.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

class Main:
    def __init__(self):
        self._isRunning = True


    def execute(self):
        while self._isRunning:
            print("Running...")


if __name__ == '__main__':
    main = Main()

    main.execute()
