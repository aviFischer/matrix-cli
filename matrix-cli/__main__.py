import sys
import argparse

from .matrix import Matrix

def parse_args():
    parser = argparse.ArgumentParser(description='Enter the command for the matrix cli')
    parser.add_argument('--output',
                        help='Name of the file to save the output to, exclude if you want it to be printed to the terminal',
                        action='store',
                        default='',
                        type=str)
    subparsers = parser.add_subparsers(help='Operation to perform', dest='command')

    to_RREF_parser = subparsers.add_parser('to-rref')
    to_RREF_parser.add_argument('--input-matrix',
                                action='store',
                                type=str,
                                default='')

    return(parser.parse_args(sys.argv[1:]))

if __name__ == '__main__':
    args = parse_args()
    print(args)
