#!/usr/bin/env python3
from gendiff import generate_diff


def main():
    file1 = '/home/alaev/python-project-50/tests/fixtures/file1.yml'
    file2 = '/home/alaev/python-project-50/tests/fixtures/file2.yml'
    diff = generate_diff(file1, file2)
    print(diff)

    file1 = '/home/alaev/python-project-50/tests/fixtures/file1.json'
    file2 = '/home/alaev/python-project-50/tests/fixtures/file2.yml'
    diff = generate_diff(file1, file2)
    print(diff)

    file1 = '/home/alaev/python-project-50/tests/fixtures/file1.yaml'
    file2 = '/home/alaev/python-project-50/tests/fixtures/file2.json'
    diff = generate_diff(file1, file2)
    print(diff)


if __name__ == '__main__':
    main()
