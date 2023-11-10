#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    description = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file1', metavar='first_file')
    parser.add_argument('file2', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(generate_diff(args.file1, args.file2))


if __name__ == '__main__':
    main()
