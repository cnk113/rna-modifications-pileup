import pandas as pd
from argparse import ArgumentParser

def mapId(splice,runs):
    for overlap in splice.itertuples():
        for read in runs.itertuples():
            if overlap.readId == read.read_id[:18]:
                print(read.filename)
                break

def parse_args():
    parser = ArgumentParser(description='gets the filenames of the reads to download')
    parser.add_argument('-splice',help='splice sites')
    parser.add_argument('-runs',help='nanopore runs')
    return parser.parse_args()

def main():
    opts = parse_args()
    splice = pd.read_csv(opts.splice,delimiter=',',header=None,index_col=False,names=['readId','chr','end','pos'])
    runs = pd.read_csv(opts.runs,delim_whitespace=True)
    mapId(splice,runs)

if __name__ == '__main__':
   main()
