#!/usr/bin/env python3
import argparse
from gendiff import generate_diff, stylish


def create_parser():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file1', metavar='first_file')
    parser.add_argument('file2', metavar='second_file')
    parser.add_argument('-f', '--format', dest='format',
                        default=stylish, type=str,
                        help='output format (default: "stylish")')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    data1 = args.file1
    data2 = args.file2
    if args.format == 'stylish':
        print(stylish(generate_diff(data1, data2), data1, data2))
    else:
        print(args.format(generate_diff(data1, data2), data1, data2))


if __name__ == '__main__':
    main()
