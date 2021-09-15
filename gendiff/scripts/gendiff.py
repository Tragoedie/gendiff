#!/usr/bin/env python3
"""This is start gendiff."""
import argparse

from gendiff.gendiff_engine import generate_diff


def main():
    """Print difference of two file."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()