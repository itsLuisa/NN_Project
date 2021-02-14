cat $1 | grep -v "^#" | sed 's/ /|/g' | sed 's/|\+/\t/g' | cut -d$'\t' -f3,4,5 | sed 's/^$/*/' > $2
