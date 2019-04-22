from argparse import ArgumentParser


def parseArgs():
    parser = ArgumentParser(description='')
    parser.add_argument('-f',help='')
    parser.add_argument('-r',help='')
    return parser.parse_args()

def main():
    opts = parseArgs()
    with open(opts.r) as infile:
        reads = {}
        for line in infile:
            line = line.rstrip().split(',')
            reads[line[0][:18]] = True
    with open(opts.f) as infile:
        window = [] 
        for line in infile:
            line = line.rstrip()
            if len(window) == 4:
                if reads.get(window[0][1:19]) != None:
                    print('\n'.join(window))
                window = [line]
            else:
                window.append(line)

if __name__ == "__main__":
    main()
