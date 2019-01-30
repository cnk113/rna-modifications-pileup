import pandas as pd
from argparse import ArgumentParser

def mapId(splice,runs,links):
    run2read = {}
    for read in runs.itertuples():
        run2read[read.read_id[:18]] = read.filename
    link2full = {}
    with open(links, "r") as ins:
        for line in ins:
            line = line.rstrip('\n')
            link2full[line.split('/')[-1]] = line
    for overlap in splice.itertuples():
        reads = run2read.get(overlap.readId)
        if reads != None:
           link = link2full.get(reads)
           if link != None:
               print(','.join([overlap.readId,overlap.ch,str(overlap.end),str(overlap.pos),link]))
    

def parse_args():
    parser = ArgumentParser(description='')
    parser.add_argument('-splice',help='splice sites')
    parser.add_argument('-runs',help='nanopore runs')
    parser.add_argument('-links',help='links to fast5')
    return parser.parse_args()

def main():
    opts = parse_args()
    splice = pd.read_csv(opts.splice,delimiter=',',header=None,index_col=False,names=['readId','ch','end','pos'])
    runs = pd.read_csv(opts.runs,delim_whitespace=True)
    mapId(splice,runs,opts.links)

if __name__ == '__main__':
   main()
