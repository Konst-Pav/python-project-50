#!/usr/bin/env python3
import argparse
import json


def generate_diff(file_path_1, file_path_2):
    file1 = json.load(open(file_path_1))
    file2 = json.load(open(file_path_2))
    all_keys = set()
    all_keys.update(file1.keys())
    all_keys.update(file2.keys())
    all_keys = list(all_keys)
    all_keys.sort()
    result = []
    for key in all_keys:
        result.append(compare(key, file1, file2))
    return '\n'.join(result)


def compare(key, file1, file2):
    value1 = file1.get(key)
    if isinstance(value1, bool):
        value1 = str(value1).lower()
    value2 = file2.get(key)
    if isinstance(value2, bool):
        value2 = str(value2).lower()
    if (value1 is not None) and (value2 is None):
        return f'- {key}: {value1}'
    if (value1 is None) and (value2 is not None):
        return f'+ {key}: {value2}'
    if value1 == value2:
        return f'  {key}: {value1}'
    if value1 != value2:
        return f'- {key}: {value1}\n+ {key}: {value2}'


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
