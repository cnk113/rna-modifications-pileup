'''
Chang Kim
'''
import re
from argparse import ArgumentParser

def parse_args():
    '''
    Argument parser
    '''
    parser = ArgumentParser(description="parses pileup for mismatches")
    parser.add_argument('-p', help='mpileup input')
    parser.add_argument('-c', help='coord')
    return parser.parse_args()

def getFreq(window):
    '''
    returns the highest 5mer mm and deletion freq as well as the 5mer
    '''
    for i in range(len(window)):
        mm = len(re.findall('[\*-]',window[i][4]))
        filtered = re.sub('-[0-9]+[ACGTNacgtn]+','',window[i][4])
        mm += len(re.findall('[ACGTNacgtn]',filtered))
        window[i].append(mm)
    highest = 0
    for i in range(5):
        mm = cov = 0
        seq = ''
        for row in window[i:i+5]:
            seq += row[2]
            cov += int(row[3])
            mm += row[6]
        freq = mm/cov
        if highest <= freq:
            highest = freq
            highestSeq = seq
    return highest, highestSeq

def parsePileup(pup,coord):
    sites = {}
    with open(coord) as infile:
        for line in infile:
            attr = line.rstrip().split(',')
            sites[(attr[1],attr[3])] = sites.get((attr[1],attr[3]),0) + 1 
    for key in list(sites):
        if sites.get(key) < 6:
            sites.pop(key)
    with open(pup) as infile:
        window = []
        hit = False
        for line in infile:
            col = line.rstrip().split()
            if int(col[3]) >= 20:
                window.append(col)
                if len(window) > 10:
                    window = window[1:]
                if hit:
                    distSite += 1
                    if distSite == 4:
                        freq, kmer = getFreq(window)
                        print(ch + ',' + pos + ',' + str(freq) + ',' + kmer)
                        hit = False
                elif sites.get((col[0],col[1])) != None:
                    ch = col[0]
                    pos = col[1]
                    distSite = 0
                    hit = True
                

def main():
    opts = parse_args()
    parsePileup(opts.p,opts.c)

if __name__ == '__main__':
    main()
