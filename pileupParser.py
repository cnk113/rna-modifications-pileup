'''
Chang Kim
'''
import re
from argparse import ArgumentParser
from pyfaidx import Fasta

def parse_args():
    '''
    Argument parser
    '''
    parser = ArgumentParser(description="parses pileup for mismatches")
    parser.add_argument('-p', help='mpileup input')
    parser.add_argument('-c', help='coord')
    parser.add_argument('-f', help='fasta')
    return parser.parse_args()

def getFreq(window):
    '''
    returns the highest 5mer mm and deletion freq as well as the 5mer
    '''
    for i in range(len(window)):
        filtered = re.sub('\+[0-9]+[ACGTNacgtn]+','',window[i][4])
        mm = len(re.findall('[ACGTNacgtn]',filtered))
        mm += len(re.findall('[\*\-]',filtered))
        window[i].append(mm)
    highest = 0
    for i in range(5):
        mm = cov = 0
        #seq = ''
        for row in window[i:i+5]:
            #seq += row[2]
            cov += int(row[3])
            mm += row[6]
        freq = mm/cov
        if highest <= freq:
            highest = freq
            #highestSeq = seq
    return highest#, highestSeq

def parsePileup(pup,coord,fasta):
    sites = {}
    prime = {}
    with open(coord) as infile:
        for line in infile:
            attr = line.rstrip().split(',')
            sites[(attr[1],attr[3])] = sites.get((attr[1],attr[3]),0) + 1 
            prime[(attr[1],attr[3])] = attr[2]
    for key in list(sites):
        if sites.get(key) < 6:
            sites.pop(key)
    hg38 = Fasta(fasta)
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
                        freq = getFreq(window)
                        if prime.get((ch,pos)) == '5':
                            kmer = hg38[ch][int(pos)-2:int(pos)+3].seq
                        else:
                            kmer = hg38[ch][int(pos)-3:int(pos)+2].seq
                        print(ch + ',' + pos + ',' + str(freq) + ',' + kmer)
                        hit = False
                elif sites.get((col[0],col[1])) != None:
                    ch = col[0]
                    pos = col[1]
                    distSite = 0
                    hit = True
                

def main():
    opts = parse_args()
    parsePileup(opts.p,opts.c,opts.f)

if __name__ == '__main__':
    main()
