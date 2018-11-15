'''
Chang Kim
'''

import pandas as pd
import numpy as np
import re
import textwrap
from argparse import ArgumentParser

def parse_args():
    '''
    Argument parser
    TODO: Search for most changed base in window
    '''
    parser = ArgumentParser(description="parses pileup for mismatches")
    parser.add_argument('-pileup', help='mpileup input')
    parser.add_argument('-output', help='filtered mismatches output')
    #parser.add_argument('-fasta', help='fasta output')
    return parser.parse_args()

def parsePileup(pileup,output):
    '''
    Parses mpileup for mismatch reads
    '''
    df = pd.read_csv(pileup, sep='\t', header=None, names=['ref_id','ref_pos','ref_base','coverage','read_base','qual'])
    df = df.drop(['qual'], axis=1) # Drops useless columns
    df = df.query('coverage >= 20') # Parses for greater than 20 depth
    df = df[df['read_base'].str.contains('G|C')] # Removes any pileups WITHOUT mismatches (Mismatches represented through "*, +, and -")
    #pileupList = zip(list(df['ref_pos']),list(df['coverage']),list(df['ref_base']),list(df['read_base'])) # Makes a list of tuples
    mmList = parse(df) # Returns a list of positional mismatches
    filtered = pd.DataFrame(mmList, columns=['chr','pos','bases','G','C','mismatches'])
    mismatchFiltered = filtered[filtered.mismatches > .3] # Filters for greater 30% mismatch frequency
    mismatchFiltered.to_csv(output,sep='\t',index=False) # Writes positions, mismatch frequency, reference bases. TODO: Most changed base in window
    '''
    baseList = zip(mismatchFiltered['pos'],mismatchFiltered['bases'])
    f = open(fasta,'w')
    for pos,bases in baseList: # Writes FASTA sequences of filtered positions with position as the header
       append = ''
       try:
          append += df.at[int(pos)+6,'bases']
          append += df.at[int(pos)+7,'bases']
       except KeyError:
          pass
       bases += append
       f.write('>' + str(pos) + '\n')
       f.write(bases+'\n')
    f.close()
    '''

def parse(pup):
    mmList = []
    for i in range(0,len(pup.index)-5,6):
        sliding = pup[i:i+6]
        window(sliding,mmList)
    return mmList

def window(sliding,mmList):
    if int(sliding.iat[0,1])+6 > int(sliding.iat[5,1]) or sliding.iat[0,0] != sliding.iat[5,0]:
        return
    totalCov = sliding['coverage'].sum()
    counts = sliding['read_base'].value_counts()
    print(counts)
    totalG = 0
    totalC = 0
    if counts.get('G') != None:
        totalG = counts['G']
    if counts.get('C') != None:
        totalC = counts['C']
    bases = ''
    for i in range(6):
        bases += sliding.iat[i,2]
    totalMm = (totalG+totalC)/totalCov
    mmList.append((sliding.iat[0,0],sliding.iat[0,1],bases,totalG,totalC,totalMm))

def main():
    opts = parse_args()
    parsePileup(opts.pileup,opts.output)

if __name__ == '__main__':
    main()
