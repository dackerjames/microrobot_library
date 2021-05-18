# KLayout DRC Checkers

Tools > DRC > Edit DRC Script, which will open the DRC editing window. Click on the "DRC" tab on the top left, then click the "import file" icon in the top left of the window to select a DRC file. This file will be copied into KLayout's program settings (so if you download a new version it will need to be imported again). 

To run a DRC script (usually on the currently open file), either click the green arrow in the DRC editing window or, in the main KLayout window, go to "Tools > DRC > ..." and select the particular DRC script to run. When complete, a DRC report window will open showing each problem (or success, sometimes, usually highlighted in green).

Sometimes an additional netlist browser window will open (usually when checking electrical connectivity; the window shows each electrically separate geometry).

## Electrical Connectivity Check

`electrical_connectivity_check.lydrc`

Can determine whether there are short circuits or open circuits in a design. See the comments inside the program for details.