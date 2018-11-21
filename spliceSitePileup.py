import pandas as pd
from argparse import ArgumentParser

def cross(introns,psl):
    for row in introns.itertuples():
        for pRow in psl.itertuples():
            if row.tName == pRow.tName:
                s


def parseArgs():
    parser = ArgumentParser(description="")
    parser.add_argument('-introns', help='')
    parser.add_argument('-psl',help='')
    return parser.parse_args()

def main():
    opts = parse_args()
    introns = pd.read_csv(introns,sep='\t',header=None,names=['tName','start','end','strand'])
    psl = pd.read_csv(psl,sep='\t',header=None,names=['qStart','qEnd','tName','tSize','tStart','tEnd','blockCount','blockSizes','qStarts','tStarts'])
    cross(introns,psl)

if __name__ == '__main__':
    main()
