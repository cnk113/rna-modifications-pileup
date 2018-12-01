import pandas as pd
from argparse import ArgumentParser

def intersect(introns,psl):
    overlaps = []
    st = {}
    for row in psl.itertuples():
        sizes = [int(n) for n in pRow.blockSizes.split(',')[:-1]]
        starts = [int(n) for n in pRow.tStarts.split(',')[:-1]]
        exons = []
        for i in range(len(starts)):
            exons.append((starts[i],starts[i]+sizes[i]))
        st[row.qName] = exons
    for row in introns.itertuples():
        for pRow in psl.itertuples():
            if row.tName in pRow.tName and row.strand == pRow.strand:
                for start,end in exons: 
                    if row.strand == '+':
                        if row.start > start and row.end > end:
                            if end - row.start >= 5:
                               overlaps.append([pRow.qName,row.tName,5,end])
                        if row.start < start and row.end < end:
                            if row.end - start >= 5:
                               overlaps.append([pRow.qName,row.tName,3,start])
                    else:
                        if row.start > start and row.end > end:
                            if end - row.start >= 5:
                               overlaps.append([pRow.qName,row.tName,3,end])
                        if row.start < start and row.end < end:
                            if row.end - start >= 5:
                               overlaps.append([pRow.qName,row.tName,5,start])
    for 
    return overlaps

def parse_args():
    parser = ArgumentParser(description="")
    parser.add_argument('-introns', help='intron coordinates')
    parser.add_argument('-psl',help='exons')
    parser.add_argument('-o',help='output file')
    return parser.parse_args()

def main():
    opts = parse_args()
    introns = pd.read_csv(opts.introns,delim_whitespace=True,header=None,index_col=False,names=['tName','start','end','strand'])
    psl = pd.read_csv(opts.psl,delim_whitespace=True,header=None,index_col=False,names=['matches','misMatches','repMatches','nCount','qNumInsert','qBaseInsert','tNumInsert','tBaseInsert','strand','qName','qSize','qStart','qEnd','tName','tSize','tStart','tEnd','blockCount','blockSizes','qStarts','tStarts'])
    overlaps = intersect(introns,psl)
    df = pd.Dataframe(overlaps,header=None)
    df.to_csv(opts.o,sep='\t',index=False)

if __name__ == '__main__':
    main()
