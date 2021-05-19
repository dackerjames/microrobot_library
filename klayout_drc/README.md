# KLayout DRC Checkers

These programs ("Design Rule Checking (DRC) scripts"), which are run inside of KLayout (the GDSII file editing program, https://klayout.de/), can ensure a design in a given GDSII file satisfies certain design rules (e.g., all metal features on a given layer are inset at least 5um from edges of silicon features).

## Instructions

To use one of these programs, first import it into KLayout with `Tools > DRC > Edit DRC Script`, which will open the DRC editing window. Click on the `DRC` tab on the top left, then click the `import file` icon in the top left of the window to select a DRC file. This file will be copied into KLayout's program settings (so if you download a new version it will need to be imported again [to avoid this, make a symlink from this git repository to the KLayout configuration folder; if you don't know what that means, you can safely ignore it]). 

To run a DRC script (usually on the currently open file), either click the green arrow in the DRC editing window or, in the main KLayout window, go to `Tools > DRC > ...` and select the particular DRC script to run. When complete, a DRC report window will open showing each problem (or success, sometimes, usually highlighted in green).

Sometimes an additional netlist browser window will open (usually when checking electrical connectivity; the window shows each electrically separate geometry).

## Area and Coverage Check

`area_coverage_check.lydrc`

Can measure the area of given layers and the ratio between areas (e.g., to make sure a layer covers more than a certain percentage of another layer). See the comments inside the program (e.g., when opened in KLayout's DRC script editing window) for details.

## Geometry Check

`geometry_check.lydrc`

Can make sure layers satisfy geometric constraints (e.g., features are spaced a certain distance apart, or features from one layer are contained within another with a given margin). See the comments inside the program (e.g., when opened in KLayout's DRC script editing window) for details.

## Electrical Connectivity Check

`electrical_connectivity_check.lydrc`

Can determine whether there are short circuits or open circuits in a design. See the comments inside the program (e.g., when opened in KLayout's DRC script editing window) for details.
