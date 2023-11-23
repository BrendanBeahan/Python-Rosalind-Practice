#!/usr/bin/env python3
""" Tetranucleotide frequency """

import argparse
import os
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Count nucleotide frequency. Print results. """
    args = get_args()

    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for i in args.dna:
        if i.lower() == "a":
            count_a += 1
        elif i.lower() == "c":
            count_c += 1
        elif i.lower() == "g":
            count_g += 1
        elif i.lower() == "t":
            count_t += 1


    print("A: " + str(count_a), "C: " + str(count_c), "G: " + str(count_g), "T: " + str(count_t))


# --------------------------------------------------
if __name__ == '__main__':
    main()
