# NN_Project
Just two students trying to get a neural network to work<br>

*sample.tsv:* made by using the unix the following command: $ cat sample.conll | grep -v "^#" | sed 's/ /|/g' | sed 's/|\\+/\t/g' | cut -d$'\t' -f3,4,5 | sed 's/^$/*/' > sample.tsv <br>

*get_information.py:* produces sample.info <br>

*sample.info:* includes information about sample.tsv <br>