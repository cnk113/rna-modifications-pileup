import pandas as pd
from argparse import ArgumentParser

def intersect(introns,psl):
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
            if intron.tName == pRow.tName and intron.strand == pRow.strand: # tName = chr
                exons = st.get(pRow.qName)
                for start,end in exons:
                    if start > intron.end: # If exon is past the intron junction
                        break 
                    if intron.strand == '+':
                        prime = 5
                        opp = 3
                    else:
                        prime = 3
                        opp = 5
                    if intron.start > start and intron.start < end: # If exon is retained in the start of an intron
                        if end - intron.start >= 10:
                            print(','.join(str(x) for x in [pRow.qName,intron.tName,prime,intron.start]))
                    if intron.end > start and intron.end < end: # If exon is retained in the end of an intron
                        if intron.end - start >= 10:
                            print(','.join(str(x) for x in [pRow.qName,intron.tName,opp,intron.end]))
            elif pRow.tName > intron.tName: # Assumes both files are sorted by chromosomes
                break

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

if __name__ == '__main__':
    main()
