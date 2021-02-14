# NN_Project
Just two students trying to get a neural network to work<br>

## Table of contents
* [General information](#general-information)
* [Data preprocessing](#data-preprocessing)

## General information
### Requirements
* python packages:
    * collections

## Data preprocessing
* *preprocessing.sh:* shell-script for preprocessing, takes input file as first argument and output file as second argument
* *sample.tsv:* created by using preprocessing.sh like this:
```
$ bash preprocessing.sh sample.conll sample.tsv
```
* *get_information.py:* produces sample.info
* *sample.info:* includes information about sample.tsv