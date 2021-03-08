from __future__ import absolute_import, division, print_function
import csv
import json
import os
import datasets
import csv

logger = datasets.logging.get_logger(__name__)


class Sample(datasets.GeneratorBasedBuilder): # wovon sollen wir erben???
    def _info(self):
        return datasets.DatasetInfo(
            description= "Dataset with words and their POS-Tags",
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "word": datasets.Value("string"),
                    "pos-tag": datasets.Value("string")
                }
            ),
            #supervised_keys=None,
            homepage="https://catalog.ldc.upenn.edu/LDC2011T03",
            citation="Weischedel, Ralph, et al. OntoNotes Release 4.0 LDC2011T03. Web Download. Philadelphia: Linguistic Data Consortium, 2011.",
        )

    def _split_generators(self, dl_manager: datasets.DownloadManager):
        loaded_files = dl_manager.download_and_extract(self.config.data_files)
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": loaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": loaded_files["test"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": loaded_files["val"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            data = csv.reader(f, delimiter="\t")
            #print(data)
            for id_, row in enumerate(data):
                if len(row) == 3:
                    yield id_, {"id": row[0], "word": row[1], "pos-tag": row[2]}

def main():
    dataset = datasets.load_dataset(
        "test.py", data_files={
            "train": "sample_train.tsv",
            "test": "sample_test.tsv",
            "val": "sample_val.tsv"
        }
    )

    print(dataset)

if __name__=="__main__":
    main()