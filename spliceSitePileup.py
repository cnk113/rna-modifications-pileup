import pandas as pd
from argparse import ArgumentParser

def binarySearch():

def intersect(introns,psl):
    overlaps = []
    st = {}
    for row in psl.itertuples():
        sizes = [int(n) for n in row.blockSizes.split(',')[:-1]]
        starts = [int(n) for n in row.tStarts.split(',')[:-1]]
        exons = []
        for i in range(len(starts)):
            exons.append((starts[i],starts[i]+sizes[i]))
        st[row.qName] = exons
    for row in introns.itertuples():
        for pRow in psl.itertuples():
            if row.tName in pRow.tName and row.strand == pRow.strand:
                exons = st.get(pRow.qName)
                for start,end in exons: 
                    if row.strand == '+':
                        prime = 5
                        opp = 3
                    else:
                        prime = 3
                        opp = 5
                    if row.start < start and row.end > start:
                        if end - row.start >= 5:
                            overlaps.append([pRow.qName,row.tName,prime,end])
                    if row.start < end and row.end > end:
                        if row.end - end >= 5:
                            overlaps.append([pRow.qName,row.tName,opp,start])
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
