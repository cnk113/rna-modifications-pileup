from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='')
    parser.add_argument('reads',help='reads')
    parser.add_argument('links',help='file links to the reads')
    return parser.parse_args()

def main():
    opts = parse_args()
    links = {}
    with open(opts.links, "r") as ins:
        for line in ins:
            line = line.rstrip('\n')
            links[line.split('/')[-1]] = line
    with open(opts.reads,"r") as f:
        for line in f:
            line = line.rstrip('\n')
            link = links.get(line)
            if link != None:
                print(link)

if __name__ == '__main__':
    main()
