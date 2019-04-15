# Chang Kim
from pyfaidx import Fasta
from argparse import ArgumentParser

def argParser():
    parser = ArgumentParser(description='')
    parser.add_argument('-reads',help='splice sites')
    parser.add_argument('-fasta',help='ref')
    parser.add_argument('-pos',help='position')
    return parser.parse_args()


def main():
    opts = argParser()
    pos = opts.pos.split(':')
    reads = []
    with open(opts.reads) as infile:
        for line in infile:
            attr = line.split(',')
            if attr[1] == pos[0] and attr[3] == pos[1]:
                reads.append(line[:18])
    headers = Fasta(opts.fasta)
    for line in reads:
        for header in headers.keys():
            if header[:18] == line:
                print('>'+header)
                print(headers[header])

if __name__ == "__main__":
    main()
