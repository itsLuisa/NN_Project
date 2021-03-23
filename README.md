# NN_Project
This is a Neural Network with an LSTM architecture for POS-Tagging.
It contains several preprocessing steps like data loading, tokenizing and embeddings borrowed from https://www.github.com/huggingface.

With our project we are addressing the research question:
How does the performance of our network differ, when provided with different amounts of data?

We therefore create different sub-datasets from the ontonetes dataset and run our model on all of them.
Details on how to recreate this can be found in the following.

## Table of contents
* [General Information](#general-information)
* [Data Preprocessing](#data-preprocessing)
* [Extracting Datasets of Different Sizes](#extracting-datasets-of-different-sizes)
* [Creating Splits](#creating-splits)
* [Data Loading](#data-loading)
* [Tokenizing](#tokenizing)
* [Embeddings](#embeddings)
* [Neural Network](#neural-network)

## General Information
### Requirements
You can either use the file [environment.yaml](environment.yaml) to build a conda environment like this:
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
* random
* numpy

After having set this up, you should be able to run all the code from this repository.

## Data Preprocessing
* *preprocessing.sh:* We use this shell-script for preprocessing. It takes an input file (.conll / .gold_conll) as first argument and output file (.tsv) as second argument, like this:
```
$ bash preprocessing.sh ontonetes.gold_conll ontonetes.tsv
```

## Extracting Datasets of Different Sizes
* *dataset_size.py:* Now it's time to choose the size of the dataset. The script takes our previously created file as input, then the name of the new, resized file and the number of lines we want to have in our new file.
  (There will be a couple of more lines in the file because the script cuts whenever the next sentence end is reached.)
```
$ python dataset_size.py ontonetes.tsv small.tsv 10000
```
* *get_information.py:* Now we can obtain valuable information about our data. This script uses an input file (small.tsv) to produce an output file (small.info), which includes useful information about the dataset.
Use it like this:
```
$ python get_information.py small.tsv small.info
```
NOTE: In our project we performed all the following steps with these dataset sizes:
* tiny: 1 000 lines
* small: 10 000 lines
* medium: 100 000 lines
* (big: 1 000 000 lines)

## Creating Splits
* *splitting_data.py:* This script will split our dataset into three splits. It uses an input file (small.tsv) to produce three output files (small_train.tsv, small_test.tsv, small_val.tsv).
Also provide the proportions by which you would like to split the input file (they have to add up to 100).
Use it like this:
```
$ python splitting_data.py small.tsv small_train.tsv small_test.tsv small_val.tsv 50:25:25
```

## Data Loading
* *data_loading.py:* This script loads the data. It will be called inside the tokenizer so no need to execute it separately.
If you still wish to, you can do it by simply providing the three splits like this:
```
$ python data_loading.py small_train.tsv small_test.tsv small_val.tsv
```

## Tokenizing
* *tokenizer.py:* This script tokenizes the data. It uses the data loading script *data_loading.py* and the tokenizer "bert-base-cased".
It will be called inside the embeddings so no need to execute it separately.
If you still wish to, you can do it by simply providing the three splits like this:
```
$ python tokenizer.py small_train.tsv small_test.tsv small_val.tsv
```

## Embeddings
* *embeddings.py:* This script creates BERT embeddings using the tokenizing tensors from the previous step.
Again, this will be called inside the Neural Network script so no need to execute it separately.
If you still wish to (but be aware that it might take a while), you can do it by simply providing the three splits like this:
```
$ python embeddings.py small_train.tsv small_test.tsv small_val.tsv
```

## Neural Network
* *Neural_Network.ipynb:* This is the actual neural network.
We put this in a jupyter notebook, so it is easier to run different parts without having to rerun everything.
To successfully run this, you need three data files containing train, test and validation split.
That means, run these files in advance:
  - *preprocessing.sh*
  - *dataset_size.py*
  - *splitting_data.py*
* The remaining files will be called in the notebook.
* To successfully run the network, insert the names of your splits at the top of the notebook
* All further instructions will be given in the notebook