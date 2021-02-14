# 1.3 get information about the data
from collections import defaultdict

with open("sample.tsv", encoding="utf-8") as f:
    sequence_length_list = list()
    tag_dict = defaultdict(int)
    for line in f:
        if "*" in line:
            sequence_length_list.append(int(previous_line.split()[0]) + 1)
        else:
            tag_dict[line.split()[2]] += 1
        previous_line = line

print(sequence_length_list)
max_length = max(sequence_length_list)
min_length = min(sequence_length_list)
mean_length = sum(sequence_length_list) / len(sequence_length_list)
number_seq = len(sequence_length_list)

print(tag_dict)

with open("sample.info", "w", encoding="utf-8") as f:
    line = "Max sequence length: " + str(max_length) + "\n"
    f.writelines(line)
    line = "Min sequence length: " + str(min_length) + "\n"
    f.writelines(line)
    line = "Mean sequence length: " + str(mean_length) + "\n"
    f.writelines(line)
    line = "Number of sequences: " + str(number_seq) + "\n"
    f.writelines(line)
    line = "\n"
    f.writelines(line)
    line = "Tags:\n"
    f.writelines(line)
    for tag in sorted(tag_dict):
        line = tag + "\t" + str(round(tag_dict[tag] / sum(tag_dict.values()) * 100, 2)) + "%" + "\n"
        f.writelines(line)
