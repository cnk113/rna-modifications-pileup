import urllib.request
import os
from argparse import ArgumentParser


def download(reads,pos,directory):
    positions = pos.split(':')
    with open(reads) as infile:
        for line in infile:
            attr = line.split(',')
            if int(attr[3]) == int(positions[1]) and attr[1] == positions[0]:
                filename = os.path.join(directory,attr[4].rstrip().split('/')[-1])
                urllib.request.urlretrieve(attr[4].rstrip(),filename)
    

def argParser():
    parser = ArgumentParser(description='')
    parser.add_argument('-reads',help='reads')
    parser.add_argument('-direct',help='output directory')
    parser.add_argument('-position', help='chr3:123213')
    return parser.parse_args()


def main():
    opts = argParser()
    cwd = os.getcwd()
    cwd = os.path.join(cwd,opts.direct)
    if not os.path.isdir(cwd):
        os.makedirs(cwd)
    download(opts.reads,opts.position,cwd)

if __name__ == '__main__':
    main()
