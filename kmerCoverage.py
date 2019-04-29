from argparse import ArgumentParser

def parseArgs():
    parser = ArgumentParser(description='')
    parser.add_argument('-i',help='')
    parser.add_argument('-d',help='')
    return parser.parse_args()

def main():
    opts = parseArgs()
    kmerMm = {}
    kmerCov = {}
    with open(opts.i,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[-1].upper()
            kmerMm[kmer] = 0
            kmerCov[kmer] = 0
    with open(opts.i,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[-1].upper()
            kmerCov[kmer] += int(col[-2])
            kmerMm[kmer] += int(col[-3])
    with open(opts.d,"r") as infile:
        for line in infile:
            col = line.rstrip().split(',')
            kmer = col[-1].upper()
            if kmerCov.get(kmer) != 0 and kmerCov.get(kmer) != None:
                if float(col[2]) - kmerMm.get(kmer)/kmerCov.get(kmer) >= 0.2:
                    print(','.join(col) + ',' + str(kmerMm.get(kmer)/kmerCov.get(kmer)) + ',' + str(kmerMm.get(kmer)) + ',' + str(kmerCov.get(kmer)))

if __name__ == "__main__":
    main()
