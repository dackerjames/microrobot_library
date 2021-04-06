#!/usr/bin/env python3
"""
This is a test script to generate microrobot parts with the gdspy library.

Note that the gdspy library will eventually be superseded by the gdstk library
from the same authors, which is similar but uses significant compiled c code
for faster speeds. However, it requires LAPACK, which is currently not
straightforward to install on Windows.

Right now, this script follows directly from the gdspy documentation at
https://gdspy.readthedocs.io/en/stable/gettingstarted.html .
"""

import gdspy

# The GDSII file is a library, which contains multiple cells.
lib = gdspy.GdsLibrary()

# Geometry must be placed in cells.
cell = lib.new_cell('FIRST')

# Create the geometry (a single rectangle) and add it to the cell.
rect = gdspy.Rectangle((0, 0), (2, 1))
cell.add(rect)

# Create an array of rectangles!
x_spacing = 20 # (um)
y_spacing = 15 # (um)
x_offset = 5 # (um)
y_offset = -20 # (um)
for x_count in range(10): # 0 to 9
    for y_count in range(5): # 0 to 4
        rect_width = 10 + 0.9*x_count
        rect_height = 10 + 0.9 * y_count
        rect = gdspy.Rectangle( (x_offset+x_spacing*x_count, y_offset+y_spacing*y_count),
                                (x_offset+x_spacing*x_count+rect_width, y_offset+y_spacing*y_count+rect_height))
        cell.add(rect)

# Save the library in a file called 'first.gds'.
lib.write_gds('first.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('first.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer(lib)
