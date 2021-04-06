#!/usr/bin/env python3
"""
This is a test script to generate microrobot parts with the gdstk library.

Right now, this follows directly from the gdstk documentation at
https://heitzmann.github.io/gdstk/index.html .
"""

import gdstk

# The GDSII file is called a library, which contains multiple cells.
lib = gdstk.Library()

# Geometry must be placed in cells.
cell = lib.new_cell("FIRST")

# Create the geometry (a single rectangle) and add it to the cell.
rect = gdstk.rectangle((0, 0), (2, 1))
cell.add(rect)

# Save the library in a GDSII file.
lib.write_gds("first.gds")

# Optionally, save an image of the cell as SVG.
cell.write_svg("first.svg")
