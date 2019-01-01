import pandas as pd
from argparse import ArgumentParser

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
    for intron in introns.itertuples():
        for pRow in psl.itertuples():
            if intron.tName in pRow.tName and intron.strand == pRow.strand:
                exons = st.get(pRow.qName)
                for start,end in exons:
                    if start > intron.end:
                        break 
                    if intron.strand == '+':
                        prime = 5
                        opp = 3
                    else:
                        prime = 3
                        opp = 5
                    if intron.start > start and intron.start < end:
                        if start - intron.start >= 5:
                            overlaps.append([pRow.qName,intron.tName,prime,intron.start])
                    if intron.end > start and intron.end < end:
                        if end - intron.end >= 5:
                            overlaps.append([pRow.qName,intron.tName,opp,intron.end])
            elif pRow.tName > intron.tName:
                break
    return overlaps

def parse_args():
    parser = ArgumentParser(description="")
    parser.add_argument('-introns', help='intron coordinates')
    parser.add_argument('-psl',help='exons')
    return parser.parse_args()

def main():
    opts = parse_args()
    introns = pd.read_csv(opts.introns,delim_whitespace=True,header=None,index_col=False,names=['tName','start','end','strand'])
    psl = pd.read_csv(opts.psl,delim_whitespace=True,header=None,index_col=False,names=['matches','misMatches','repMatches','nCount','qNumInsert','qBaseInsert','tNumInsert','tBaseInsert','strand','qName','qSize','qStart','qEnd','tName','tSize','tStart','tEnd','blockCount','blockSizes','qStarts','tStarts'])
    overlaps = intersect(introns,psl)
    for overlap in overlaps:
        print(','.join(overlap))

if __name__ == '__main__':
    main()
