# NN_Project
Just two students trying to get a neural network to work.<br>
More detailed description will follow.

## Table of contents
* [General information](#general-information)
* [Data preprocessing](#data-preprocessing)

## General information
### Requirements
You can either use the file *environment.yaml* to build a conda environment like this:
```
$ conda env create --file environment.yaml
$ conda activate Valentina_Luisa
```
or install the following python packages by hand:
* collections
* sys

After having set this up, you should be able to run all the code from this repository.

## Data preprocessing
* *preprocessing.sh:* shell-script for preprocessing, takes input file as first argument and output file as second argument, like this:
```
$ bash preprocessing.sh sample.conll sample.tsv
```
* *get_information.py:* uses an input file (sample.tsv) to produce an output file (sample.info), which includes useful information about the dataset.
Use it like this:
```
$ python get_information.py sample.tsv sample.info
```