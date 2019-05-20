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
            if kmerM.get(kmer) != 0 and kmerM.get(kmer) != None:
                print(','.join(col) + ',' + str(kmerMm.get(kmer)/(kmerM.get(kmer)+kmerMm.get(kmer))) + ',' + str(kmerMm.get(kmer)) + ',' + str(kmerM.get(kmer)))

if __name__ == "__main__":
    main()
