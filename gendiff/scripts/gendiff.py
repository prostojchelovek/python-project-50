#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def create_parser():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file1', metavar='first_file')
    parser.add_argument('file2', metavar='second_file')
    parser.add_argument('-f', '--format', dest='format',
                        default='stylish', type=str,
                        help='output format (default: "stylish")')

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    data1 = args.file1
    data2 = args.file2
    if args.format == 'plain':
        print(generate_diff(data1, data2, 'plain'))
    elif args.format == 'stylish':
        print(generate_diff(data1, data2))
    elif args.format == 'json':
        print(generate_diff(data1, data2, 'json'))


if __name__ == '__main__':
    main()
