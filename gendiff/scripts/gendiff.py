#!/usr/bin/env python3
import argparse
from gendiff.parser import parse_data
from gendiff.formatter import format_diff


def generate_diff(path_to_file1, path_to_file2, formatter_name='stylish'):
    diff = parse_data(path_to_file1, path_to_file2)
    return format_diff(diff, formatter_name)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", type=str, help='output format (default: "stylish")', default='stylish')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
