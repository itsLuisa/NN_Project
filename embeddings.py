from tokenizer import tokenize_and_encode, initialize_tokenizer
from transformers import BertTokenizer, BertModel
from datasets import load_dataset
import sys
import torch

def initialize_model():
    model = BertModel.from_pretrained("bert-base-cased")
    return model

def embedding_model(model, encodings):
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
    tokenizer = initialize_tokenizer()
    all_encodings_train = tokenize_and_encode("train", data_sets, tokenizer)

    model = initialize_model()
    for sentence in all_encodings_train:
        print(embedding_model(model, sentence["input_ids"]))

if __name__ == "__main__":
    main()
