import pandas as pd
from argparse import ArgumentParser

def mapId(splice,runs):
    run2read = {}
    for read in runs.itertuples():
        run2read[read.read_id[:18]] = read.filename
    for overlap in splice.itertuples():
        if run2read.get(overlap.readId) != None:
           print(read.filename)

def parse_args():
    parser = ArgumentParser(description='')
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
