from transformers import BertTokenizer
from datasets import load_dataset
import sys

def tokenize_and_encode(split, data_sets):
    tz = BertTokenizer.from_pretrained("bert-base-cased")
    all_encodings = list()
    for sentence in data_sets[split]["tokens"]:
        if sentence:
            encoded = tz.encode_plus(
                text=sentence,
                is_split_into_words=True,
                add_special_tokens=True,
                truncation=True,
                max_length=73,
                padding="max_length",
                return_attention_mask=True,
                return_tensors="pt"
            )
            all_encodings.append(encoded)
    return all_encodings

def encode_pos(split, data_sets):
    tz = BertTokenizer.from_pretrained("bert-base-cased")
    all_encodings = list()
    for sentence in data_sets[split]["pos_tags"]:
        if sentence:
            encoded = tz.encode_plus(
                text=sentence,
                is_split_into_words=True,
                add_special_tokens=True,
                truncation=True,
                max_length=73,
                padding="max_length",
                return_attention_mask=True,
                return_tensors="pt"
            )
            all_encodings.append(encoded)
    return all_encodings

def main():
    training_file = sys.argv[1]
    test_file = sys.argv[2]
    validation_file = sys.argv[3]

    data_files = {
                "train": training_file,
                "test": test_file,
                "validation": validation_file
            }

    data_sets = load_dataset("data_loading.py", data_files=data_files)

    all_encodings_train = tokenize_and_encode("train", data_sets)
    all_encodings_test = tokenize_and_encode("test", data_sets)
    all_encodings_validation = tokenize_and_encode("validation", data_sets)

    pos_encoded_train = encode_pos("train", data_sets)
    pos_encoded_test = encode_pos("test", data_sets)
    pos_encoded_validation = encode_pos("validation", data_sets)

    print(all_encodings_validation[0])
    print(pos_encoded_validation[0])

if __name__ == "__main__":
    main()
