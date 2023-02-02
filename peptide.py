import gzip


def main():
    aa = dict()
    counter = 0  # for counting number of sequences in a file
    counterF = 0  # for counting number of residue in a file
    file = input("Enter FASTA File Location: ")  # ask user for input file location
    fileFo = file[len(file) - 2]  # check for file format
    fileFo = fileFo.lower().rstrip()

    if fileFo == 'g':  # if gz-format open using gzip
        f = gzip.open(file, 'rt')
    else:
        f = open(file, 'r')

    for line in f:
        if line.startswith('>'):
            counter += 1
            continue
        else:
            line = line.upper().rstrip()

            for base in line:
                if base in aa:
                    aa[base] += 1
                    counterF += 1
                else:
                    aa[base] = 1
                    counterF += 1

    print('Total sequences found: ' + str(counter))
    print('Total residues found: ' + str(counterF))


if __name__ == '__main__':
    main()
