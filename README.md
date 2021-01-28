# NN_Project
Just two students trying to get a neural network to work<br>

sample.csv: made by using the unix the following command: $ cat sample.conll | grep -v "#" | sed 's/ /|/g' | sed 's/|\+/\t/g' | cut -d$'\t' -f3,4,5 | sed 's/^$/\t\t*/' > sample.tsv