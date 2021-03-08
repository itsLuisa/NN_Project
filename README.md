# NN_Project
Just two students trying to get a neural network to work.<br>
More detailed description will follow.

## Table of contents
* [General Information](#general-information)
* [Data Preprocessing](#data-preprocessing)
* [Creating Splits](#creating-splits)
* [Data Loading](#data-loading)

## General Information
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

## Data Preprocessing
* *preprocessing.sh:* shell-script for preprocessing, takes input file as first argument and output file as second argument, like this:
```
$ bash preprocessing.sh sample.conll sample.tsv
```
* *get_information.py:* uses an input file (sample.tsv) to produce an output file (sample.info), which includes useful information about the dataset.
Use it like this:
```
$ python get_information.py sample.tsv sample.info
```

## Creating Splits
* *splitting_data.py:* uses an input file (sample.tsv) to produce three output files (sample_train.tsv, sample_test.tsv, sample_val.tsv).
Also provide the proportions by which you would like to split the input file (they have to add up to 100 in order for every line of the input file to be in one of the output files).
Use it like this:
```
$ python splitting_data.py sample.tsv sample_train.tsv sample_test.tsv sample_val.tsv 60:20:20
```
TODO: set encodings right

## Data Loading
* *data_loading.py:* Still in progress, still facing a windows permission error.
* *tokenizer.py:* To be uploaded, still suffers from the error in *data_loading.py*.
Also: HfArgumentParser (line 150) is not happy with .tsv-files. Use .csv instead?<br>
Used script from:
https://github.com/huggingface/transformers/blob/master/examples/token-classification/run_ner.py <br>
and made changes in:
  - line 213, 217: data loading
  - line 227, 229: column naming