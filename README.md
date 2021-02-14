# NN_Project
Just two students trying to get a neural network to work<br>

## Table of contents
* [Requirements]
* [Files]

## Requirements
* python package collections

## Files
* *sample.tsv:* made by using the unix the following command:
'''
$ cat sample.conll | grep -v "^#" | sed 's/ /|/g' | sed 's/|\\+/\t/g' | cut -d$'\t' -f3,4,5 | sed 's/^$/*/' > sample.tsv
'''

* *get_information.py:* produces sample.info

* *sample.info:* includes information about sample.tsv