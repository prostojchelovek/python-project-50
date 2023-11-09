#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('file1', metavar='first_file')
    parser.add_argument('file2', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()


def generate_diff(file1, file2):
    result = ''
    input1 = json.load(open(file1))
    input2 = json.load(open(file2))
    set_keys1 = set(input1)
    set_keys2 = set(input2)
    only_in_file1 = set_keys1.difference(set_keys2)
    only_in_file2 = set_keys2.difference(set_keys1)
    file_intersection = set_keys1.intersection(set_keys2)
    all_keys = sorted(list(set_keys1.union(set_keys2)))
    for elem in all_keys:
        if elem in only_in_file1:
            result += f"  - {elem}: {input1[elem]}\n"
        elif elem in only_in_file2:
            result += f"  + {elem}: {input2[elem]}\n"
        elif elem in file_intersection and input1[elem] == input2[elem]:
            result += f"    {elem}: {input1[elem]}\n"
        else:
            result += f"  - {elem}: {input1[elem]}\n  + {elem}: {input2[elem]}\n"
    return '{\n' + result + '}\n'


if __name__ == '__main__':
    main()
