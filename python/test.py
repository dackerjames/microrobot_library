#!/usr/bin/env python3
"""
This is a test script to generate microrobot parts with the gdspy library.

The gdspy library will eventually be superseded by the gdstk library,
which is similar but uses significant compiled c code for faster speeds.
However, it requires LAPACK, which is currently not straightforward to
install on Windows.

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

# Save the library in a file called 'first.gds'.
lib.write_gds('first.gds')

# Optionally, save an image of the cell as SVG.
cell.write_svg('first.svg')

# Display all cells using the internal viewer.
gdspy.LayoutViewer(lib)
