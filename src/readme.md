# Readme

This folder contains PRISM code for all of the case study models I'm developing.

An overview of the current folder structure:
* `ShutTheBox` - models, property files and data files for the Shut the Box game.
* `LiarsDice` - models for Liar's Dice.
* `26Point2` - models for 26.2.
* `utils` - a collection of Python scripts designed to automate the process of generating PRISM models. (model-specific processing is provided in that model's folder, while the `utils` folder focuses on common aspects of preprocessing).

## Build instructions

A series of Jupyter notebooks are provided in order to run model checking operations automatically. These notebooks build the models using the tools in the `utils` folder, perform model checking, store the results to data files, and generate visualisations in the case of Shut the Box. These notebooks contain cells to define parameters for the model - change these to build different models.

Note: Model checking here is tested on PRISM-games 3.0, along with PRISM 4.4.pomdps, the extension version of PRISM with support for POMDPs. PRISM 4.7 should work for the latter, although this hasn't been tested yet.
