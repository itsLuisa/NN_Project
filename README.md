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
If you still wish to, you can do it  by simply providing the three splits like this:
```
$ python data_loading.py sample_train.tsv sample_test.tsv sample_val.tsv
```

## Tokenizing
* *tokenizer.py:* Used script from:
https://github.com/huggingface/transformers/blob/master/examples/token-classification/run_ner.py <br> 
TODO: work on how to pass own data loading script. Is it possible without changing the original code?<br>
Also: HfArgumentParser (line 171) is not happy with .tsv-files. Use .csv instead?<br>
Made one small change in line 238 because we want to use our own data loading script but also local files,
which cannot be specified with any argument when calling the original script. <br>
Could not get it to work with tsv-files yet, but we can simply substitute the suffixes of the output files with .csv in the [Creating Splits](#creating-splits) step.<br>
A lot of variables can be specified here, but for now we use the tokenizer like this:
```
$ python tokenizer.py --model_name_or_path "bert-base-uncased" --output_dir ./ --task_name pos --train_file sample_train.csv --test_file sample_test.csv --validation_file sample_val.csv
```
## Embeddings
* TODO