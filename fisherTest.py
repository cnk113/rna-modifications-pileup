import scipy.stats as stats
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="")
    parser.add_argument('-i', help='takes in input from kmerCoverage.py')
    parser.add_argument('-a', help='input from allKmerCoverage.py')
    return parser.parse_args()

def main():
    opts = parse_args()
    kmer = {}
    with open(opts.a,"r") as infile:
        for line in infile:
            col = line.rstrip().split()
            kmer[col[0]] = col[1]
    with open(opts.i,"r") as infile:
        total = []
        for line in infile:
            col = line.rstrip().split(',')
            if kmer.get(col[2]) != None:
                if float(col[4]) - float(col[7]) >= 0.05:
                    table = [[int(col[5]),int(col[6])], [int(col[8]),int(col[9])]]
                    oddsratio, pvalue = stats.fisher_exact(table)
                    col.append(kmer.get(col[2]))
                    col.append(pvalue)
                    if pvalue <= 0.05:
                        total.append(col)
    sp = sorted(total, key=lambda x: x[11])
    #print("chr\tpos\tkmer\tprime\tdRNAfrequency\tdRNAmismatch\tdRNAmatch\tIVTfrequency\tIVTmismatch\tIVTmatch\tallPvalue\tpValue")
    for col in sp:
        print('\t'.join(str(x) for x in col))

if __name__ == '__main__':
    main()
