from argparse import ArgumentParser
import scipy.stats as stats

def parse_args():
    parser = ArgumentParser(description='')
    parser.add_argument('-i',help='')
    parser.add_argument('-d',help='')
    return parser.parse_args()

def main():
    opts = parse_args()
    kmerMm = {}
    kmerM = {}
    directMm = {}
    directM = {}
    with open(opts.i,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[2].upper()
            kmerMm[kmer] = 0
            kmerM[kmer] = 0
    with open(opts.i,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[2].upper()
            kmerM[kmer] += int(col[6])
            kmerMm[kmer] += int(col[5])
    with open(opts.d,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[2].upper()
            directMm[kmer] = 0
            directM[kmer] = 0
    with open(opts.d,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[2].upper()
            directM[kmer] += int(col[6])
            directMm[kmer] += int(col[5])
    p = {}
    for key in directM:
        if kmerM.get(key) != None:
            table = [[kmerM.get(key),directM.get(key)], [kmerMm.get(key),directMm.get(key)]]
            oddsratio, pvalue = stats.fisher_exact(table)
            p[key] = pvalue
    sp = sorted(p.items(), key=lambda kv: kv[1])
    for tup in sp:
        print(tup[0] + '\t' + str(tup[1]))

if __name__ == "__main__":
    main()
