import sys

def sizing_the_data(dataset, new_data, size):
    n = 0
    stop = False
    with open(new_data, "w", encoding="utf-8") as g:
        with open(dataset, encoding="utf-8") as f:
            for line in f:
                n += 1
                if n <= size:
                    g.writelines(line)
                else:
                    if stop == False:
                        if line == "*\n":
                            stop = True
                            g.writelines(line)
                        else:
                            g.writelines(line)
                    if stop == True:
                        break
    print(n)

def main():
    # 2 294 841 lines in ontonetes.tsv
    dataset = sys.argv[1]
    new_data = sys.argv[2]
    size = int(sys.argv[3])
    sizing_the_data(dataset, new_data, size)

if __name__=="__main__":
    main()
