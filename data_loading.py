import datasets
import csv

logger = datasets.logging.get_logger(__name__)


class SampleConfig(datasets.BuilderConfig):

    def __init__(self, **kwargs):
        super(SampleConfig, self).__init__(**kwargs)


class Sample(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        SampleConfig(name="conll2003", version=datasets.Version("1.0.0"), description="Conll2003 dataset"),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description="Dataset with words and their POS-Tags",
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "pos_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "''",
                                ",",
                                "-LRB-",
                                "-RRB-",
                                ".",
                                ":",
                                "CC",
                                "CD",
                                "DT",
                                "EX",
                                "FW",
                                "HYPH",
                                "IN",
                                "JJ",
                                "JJR",
                                "JJS",
                                "MD",
                                "NN",
                                "NNP",
                                "NNPS",
                                "NNS",
                                "PDT",
                                "POS",
                                "PRP",
                                "PRP$",
                                "RB",
                                "RBR",
                                "RBS",
                                "RP",
                                "TO",
                                "UH",
                                "VB",
                                "VBD",
                                "VBG",
                                "VBN",
                                "VBP",
                                "VBZ",
                                "WDT",
                                "WP",
                                "WRB",
                                "``"
                            ]
                        )
                    ),
                }
            ),
            supervised_keys=None,
            homepage="https://catalog.ldc.upenn.edu/LDC2011T03",
            citation="Weischedel, Ralph, et al. OntoNotes Release 4.0 LDC2011T03. Web Download. Philadelphia: Linguistic Data Consortium, 2011.",
        )

    def _split_generators(self, dl_manager):
        loaded_files = dl_manager.download_and_extract(self.config.data_files)
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": loaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": loaded_files["test"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": loaded_files["val"]})
        ]

    def _generate_examples(self, filepath):
        logger.info("generating examples from = %s", filepath)
        with open(filepath, encoding="cp1252") as f:
            data = csv.reader(f, delimiter="\t")
            ids = list()
            tokens = list()
            pos_tags = list()
            for id_, line in enumerate(data):
                #print(line)
                if len(line) == 1:
                    if tokens:
                        yield id_, {"id": ids, "tokens": tokens, "pos_tags": pos_tags}
                        ids = list()
                        tokens = list()
                        pos_tags = list()
                else:
                    ids.append(line[0])
                    tokens.append(line[1])
                    pos_tags.append(line[2])
            # last example
            yield id_, {"id": ids, "tokens": tokens, "pos_tags": pos_tags}


def main():
    dataset = datasets.load_dataset(
        "data_loading.py", data_files={
            "train": "train.tsv",
            "test": "test.tsv",
            "val": "val.tsv"
        }
    )

    #print(dataset)

if __name__=="__main__":
    main()
