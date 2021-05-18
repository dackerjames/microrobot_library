# microrobot_library

This is a set of programs to aid in MEMS microrobot design and layout. They are not specific to any one project and are intended to be flexible enough for multiple applications (e.g., different microfabrication recipes).

## Layout Generation

These programs can generate a 2D design with microfabricated structures (e.g., a complete electrostatic inchworm motor) given only a few parameters.

The `matlab` folder contains a MATLAB library with scripts that can generate 2D layout files for a wide range of microfabricated structures, from rectangles with etch holes to complete electrostatic inchworm motors. See `matlab/README.md` for more information.

The `python` folder contains the beginnings of a python library with scripts that do the same. Using python rather than MATLAB may allow easier integration with external programs in the future.

## DRC (design rule checkers)

These programs can ensure a design in a given GDSII file satisfies certain constraints (e.g., all metal features on a given layer are inset at least 5um from edges of silicon features).

The `klayout_drc` folder contains DRC programs for KLayout (https://klayout.de/), the 2D GDSII file editing program.
