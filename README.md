# NN_Project
Just two students trying to get a neural network to work.<br>
More detailed description will follow.

## Table of contents
* [General Information](#general-information)
* [Data Preprocessing](#data-preprocessing)
* [Creating Splits](#creating-splits)
* [Data Loading](#data-loading)
* [Tokenizing](#tokenizing)
* [Embeddings](#embeddings)
* [Neural Network](#neural-network)

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
* datasets
* seqeval
* transformers
* torch
* matplotlib

After having set this up, you should be able to run all the code from this repository.

## Data Preprocessing
* *preprocessing.sh:* Shell-script for preprocessing, takes input file as first argument and output file as second argument, like this:
```
$ bash preprocessing.sh sample.conll sample.tsv
```
* *get_information.py:* Uses an input file (sample.tsv) to produce an output file (sample.info), which includes useful information about the dataset.
Use it like this:
```
$ python get_information.py sample.tsv sample.info
```

## Creating Splits
* *splitting_data.py:* Uses an input file (sample.tsv) to produce three output files (sample_train.tsv, sample_test.tsv, sample_val.tsv).
Also provide the proportions by which you would like to split the input file (they have to add up to 100 in order for every line of the input file to be in one of the output files).
Use it like this:
```
$ python splitting_data.py sample.tsv sample_train.tsv sample_test.tsv sample_val.tsv 60:20:20
```


## Data Loading
* *data_loading.py:* Loads the data. Will be called inside the tokenizer so no need to execute it separately.
If you still wish to, you can do it by simply providing the three splits like this:
```
$ python data_loading.py sample_train.tsv sample_test.tsv sample_val.tsv
```

## Tokenizing
* *tokenizer.py:* Tokenizes the data. It uses the data loading script *data_loading.py* and the tokenizer "bert-base-cased".
Will be called inside the embeddings so no need to execute it separately.
If you still wish to, you can do it by simply providing the three splits like this:
```
$ python tokenizer.py sample_train.tsv sample_test.tsv sample_val.tsv
```

## Embeddings
* *embeddings.py:* Creates BERT embeddings using the tokenizing tensors from the previous step.
Again, this will be called inside the Neural Network script so no need to execute it separately.
If you still wish to (but be aware that it might take a while), you can do it by simply providing the three splits like this:
```
$ python embeddings.py sample_train.tsv sample_test.tsv sample_val.tsv
```

## Neural Network
* *Neural_Network.ipynb:* This is the actual neural network.
We put this in a jupyter notebook, so it is easier to run different parts without having to rerun everything.
To successfully run this, you need three data files containing train, test and validation split.
That means, run these files in advance:
  - *preprocessing.sh*
  - *splitting_data.py*
* The remaining files will be called in the notebook.
* NOTE: Still incomplete
* CURRENT STATE: Decided on LSTM for the architecture and are still trying to implement it so that it works.
We are unsure about where to incorporate the embeddings. This and other questions are further explained in the notebook.