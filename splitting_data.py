import sys

def split(file, train_file, test_file, val_file, proportions):
    proportions = [int(i) / 100 for i in proportions]
    with open(file, encoding="utf-8") as f:
        for id, line in enumerate(f):
            pass
    print("length of the whole file:", id)
    len_train = id * proportions[0]
    len_test = id * proportions[1]
    len_val = id * proportions[2]
    print("approx. length of the splits:", len_train, len_test, len_val)
    with open(file, encoding="utf-8") as f:
        for id, line in enumerate(f):
            if id <= len_train:
                flag = "training"
                with open(train_file, "a", encoding="utf-8") as train:
                    train.writelines(line)

            elif id > len_train and id <= (len_train+len_test):
                if flag == "training":
                    if line == "*\n":
                        flag = "testing"
                        with open(train_file, "a", encoding="utf-8") as train:
                            train.writelines(line)
                    else:
                        with open(train_file, "a", encoding="utf-8") as train:
                            train.writelines(line)
                else:
                    with open(test_file, "a", encoding="utf-8") as test:
                        test.writelines(line)

            elif id > (len_train+len_test):
                if flag == "testing":
                    if line == "*\n":
                        flag = "validation"
                        with open(test_file, "a", encoding="utf-8") as test:
                            test.writelines(line)
                    else:
                        with open(test_file, "a", encoding="utf-8") as test:
                            test.writelines(line)
                else:
                    with open(val_file, "a", encoding="utf-8") as val:
                        val.writelines(line)
    return train_file, test_file, val_file

def main():
    file = sys.argv[1]
    train_file = sys.argv[2]
    test_file = sys.argv[3]
    val_file = sys.argv[4]
    proportions = sys.argv[5]
    #file = "sample.tsv"
    proportions = proportions.split(":")

    with open(train_file, "w", encoding="utf-8"):
        pass
    with open(test_file, "w", encoding="utf-8"):
        pass
    with open(val_file, "w", encoding="utf-8"):
        pass
    split(file, train_file, test_file, val_file, proportions)

if __name__=="__main__":
    main()