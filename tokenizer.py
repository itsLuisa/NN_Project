from transformers import BertTokenizer
from datasets import load_dataset
import sys

def initialize_tokenizer():
    tz = BertTokenizer.from_pretrained("bert-base-cased")
    return tz

def tokenize_and_encode(split, data_sets, tokenizer):
    tz = tokenizer
    all_encodings = list()
    for sentence in data_sets[split]["tokens"]:
        if sentence:
            ids = tz.convert_tokens_to_ids(sentence)
            encoded = tz.encode_plus(
                text=ids,
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

def encode_pos(split, data_sets, tokenizer):
    tz = tokenizer
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

    # initialize the tokenizer
    tz = initialize_tokenizer()

    all_encodings_train = tokenize_and_encode("train", data_sets, tz)
    pos_encoded_train = encode_pos("train", data_sets, tz)

    print(all_encodings_train[0])
    print(pos_encoded_train[0])

if __name__ == "__main__":
    main()
