from pyfaidx import Fasta
from argparse import ArgumentParser
import pandas as pd


def appendSeq(hg38,splice):
    splice = splice.drop_duplicates(subset='pos')
    for row in splice.itertuples():
        print(hg38[row.ch][row.pos-5:row.pos+5].seq)

def argParser():
    parser = ArgumentParser(description='')
    parser.add_argument('-splice',help='splice sites')
    parser.add_argument('-fasta',help='ref')
    return parser.parse_args()

def main():
    opts = argParser()
    hg38 = Fasta(opts.fasta)
    splice = pd.read_csv(opts.splice,delimiter=',',header=None,index_col=False,names=['readId','ch','end','pos'])
    appendSeq(hg38,splice)

if __name__ == "__main__":
    main()
