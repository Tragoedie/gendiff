"""This is gendiff scripts."""
import argparse

from gendiff.gendiff_engine import generate_diff


def main():
    """Print difference of two file."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        dest='format',
        action='store',
    )
    args = parser.parse_args()
    if not args.format:
        args.format = 'stylish'
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
