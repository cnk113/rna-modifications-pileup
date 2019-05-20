from argparse import ArgumentParser



def parse_args():
    parser = ArgumentParser(description='')
    parser.add_argument('-i',help='')
    parser.add_argument('-d',help='')
    return parser.parse_args()

def main():
    opts = parse_args()


if __name__ == "__main__":
    main()
