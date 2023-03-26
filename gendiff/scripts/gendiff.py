#!/usr/bin/env python3
from gendiff.gendiff_cli import parse_args
from gendiff.parser import parse_files
from gendiff.formatters.formatter import format_diff


def generate_diff(path_to_file1, path_to_file2, formatter_name='stylish'):
    diff = parse_files(path_to_file1, path_to_file2)
    return format_diff(diff, formatter_name)


def main():
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
