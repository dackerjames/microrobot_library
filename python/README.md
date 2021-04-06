# python microrobot_library

This is the potential beginning of a python library designed to aid in MEMS microrobot design and layout that works similarly to the MATLAB library.  

This repository is built upon (and requires) the `gdspy` library (https://github.com/heitzmann/gdspy), a python library capable of manipulating and generating GDSII files.

See the `gdspy` documentation at https://gdspy.readthedocs.io/en/stable/gettingstarted.html .

(Note that `gdspy` library is planned to be deprecated in the future in favor of `gdstk` by the same authors. `gdstk` uses compiled c code for extra speed, but also requires installation of the LAPACK library.)

## More detailed installation instructions

`gdspy` can be installed by using a command line window to run:

```
pip install numpy
pip install gdspy
```

Running `test.py` should produce test GDSII and SVG files.

Generated GDSII files can be opened and edited with a GDSII editor like [KLayout](https://klayout.de/).
