#!/usr/bin/env python3
import sys
from gendiff.gendiff_func import generate_diff
from gendiff.gendiff_cli import parse_args


def main():
    args = parse_args(sys.argv[1:])
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
