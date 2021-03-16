from tokenizer import tokenize_and_encode
from transformers import BertTokenizer, BertModel
from datasets import load_dataset
import sys
import torch

def embedding_model(encodings):
    model = BertModel.from_pretrained("bert-base-cased")
    with torch.no_grad():
        last_hidden_states = model(encodings)
    return last_hidden_states

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

    for sentence in all_encodings_train:
        print(embedding_model(sentence["input_ids"]))

if __name__ == "__main__":
    main()