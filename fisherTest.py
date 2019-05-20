import scipy.stats as stats
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description="")
    parser.add_argument('-i', help='takes in input from kmerCoverage.py')
    return parser.parse_args()

def main():
    opts = parse_args()
    with open(opts.i,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            table = [[int(col[7]),int(col[8])], [int(col[7]),int(col[8])]]
            oddsratio, pvalue = stats.fisher_exact(table)
            print(','.join(col) + ',' + str(pvalue))

if __name__ == '__main__':
    main()
