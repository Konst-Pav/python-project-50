#!/usr/bin/env python3
import sys
from gendiff.gendiff_cli import parse_args
from gendiff.parser import parse_files
from gendiff.formatters.formatter import format_diff


def generate_diff():
    args = parse_args(sys.argv[1:])
    diff = parse_files(args.first_file, args.second_file)
    return format_diff(diff, args.format)


def main():
    print(generate_diff())


if __name__ == '__main__':
    main()
