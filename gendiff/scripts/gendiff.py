#!/usr/bin/env python3
import sys
from gendiff.gendiff_cli import parse_args
from gendiff.parser import parse_files
from gendiff.formatters.formatter import format_diff


def generate_diff(path_to_file1, path_to_file2, formatter_name='stylish'):
    return format_diff(parse_files(path_to_file1, path_to_file2), formatter_name)


def main():
    args = parse_args(sys.argv[1:])
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
