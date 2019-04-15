

# assuming each line of the PSL is called `line`, and is rstrip()-ed
# and .split('\t')-ed, you can use this too:
from argparse import ArgumentParser
import collections, re, natsort

def parseArgs():
    parser = ArgumentParser(description='')
    parser.add_argument('-p',help='')
    parser.add_argument('-c',help='')
    return parser.parse_args()

def main():
    opts = parseArgs()
    with open(opts.p,"r") as infile:
        iCount = {}
        eCount = {}
        for line in infile:
            line = line.rstrip().split()
            sizes = [int(n) for n in line[18].split(',')[:-1]]
            starts = [int(n) for n in line[20].split(',')[:-1]]
            if len(starts) != 1:
                for b in range(len(starts)-1):
                    iCount[(line[13],starts[b]+sizes[b],starts[b+1],line[8],line[9])] = iCount.get((line[13],starts[b]+sizes[b],starts[b+1],line[8],line[9]),0) + 1
                for i in range(len(starts)):
                    eCount[(line[13],starts[i],starts[i]+sizes[i],line[8],line[9])] = eCount.get((line[13],starts[i],starts[i]+sizes[i],line[8],line[9]),0) + 1
    with open(opts.c,"r") as coord:
         c = []
         for line in coord:
             line = line.rstrip()
             c.append(tuple(line.split()))
    for intron in iCount:
        if iCount.get(intron) < 20:
            iCount.pop(intron)
        if iCount.get(intron) not in c:
            iCount.pop(intron)
    '''
    for exon in eCount:
        if eCount.get(exon) < 20:
            eCount.pop(exon)
    '''
    iCount = natsort.natsorted(iCount.keys(), key=lambda x: x[0])
    eCount = natsort.natsorted(eCount.key(), key=lambda x: x[0])
    for intron in iCount:
        for exon in eCount:
            if exon[0] == intron[0] and exon[3] == intron[3]:
                if exon[3] == '+':
                    prime = 5
                    opp = 3
                else:
                    prime = 3
                    opp = 5
                if intron[1] > exon[1] and intron[1] < exon[2]:
                    if exon[1] - intron[1] >= 5:    
                        print('\t'.join([s[0],str(s[1]),str([3])))
                if intron[2] > exon[2] and intron[2] < exon
                    if exon[2] - intron[2] >= 5:
                        print('\t'.join([s[0],str(s[1]),str(s[2]),s[3]]))
            elif exon[0] > intron[0]:
                break

if __name__ == "__main__":
   main()
