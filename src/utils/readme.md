# Utils readme

This folder contains various utilities that are used throughout the development process, such as automating experiments and constructing more complex PRISM models using preprocessing.

# PyPrism

PyPrism is a tool which accepts a partially completed PRISM model file, using the `.pyprism` extension. This file contains lines of PRISM code, along with _template instructions_ surrounded by `@` symbols, such as `@stb/cover n@` These instructions are comprised of an optional _location_, a _function_, and a collection of _parameters_ if required for the given function. In further detail:

* The _location_ represents the file where the given function is defined. If no location is defined, the function is assumed to exist in the `templates.py` file in the `utils` directory. Otherwise, the function is assumed to exist in the `templates_{location}.py` file (for instance, in `@stb/cover n@`, the `cover` function is assumed to exist in `templates_stb.py`).
* The _function_ represents the name of the function which generates PRISM model code.
* The _parameters_ are provided to the function to allow for the complexity of the model to vary based on instance size (for instance, for easily varying the number of players in an n player game). Note that template functions only support integer arguments at the moment.

Each template instruction represents a function call, and the outputted PRISM model code from that function is placed where the template instruction occurs.

## Usage

`python pyprism.py [input] [output]`.

The `input` parameter represents the filename of the `.pyprism` template file, while `output` represents the filename of the outputted `.prism` model file.