#!/usr/bin/env python3
import argparse
import json
import yaml
from yaml.loader import SafeLoader
from os.path import basename


def generate_diff(file1, file2):
    dict1 = convert_to_dict(file1)
    dict2 = convert_to_dict(file2)
    result_list = []

    def walk(arg_dict1, arg_dict2, result_list):
        all_keys = get_sorted_unique_keys(arg_dict1, arg_dict2)
        for key in all_keys:
            value1 = arg_dict1.get(key, None)
            value2 = arg_dict2.get(key, None)
            if isinstance(value1, dict) and isinstance(value2, dict):
                conclusion = ' '
                nested_result_list = []
                walk(value1, value2, nested_result_list)
                value = nested_result_list
            else:
                value = {'before': value1, 'after': value2}
                match (value1, value2):
                    case (value1, None):
                        conclusion = 'Removed'
                    case (None, value2):
                        conclusion = 'Added'
                    case (value1, value2) if value1 == value2:
                        conclusion = 'Same'
                    case (value1, value2) if value1 != value2:
                        conclusion = 'Changed'
                    case _:
                        conclusion = 'Something went wrong'
            result_list.append({'conclusion': conclusion, 'key': key, 'value': value})

    walk(dict1, dict2, result_list)
    return result_list


def get_sorted_unique_keys(dict1, dict2):
    unique_keys = set(dict1)
    unique_keys.update(dict2)
    list_unique_keys = list(unique_keys)
    list_unique_keys.sort()
    return list_unique_keys


def convert_to_dict(path_to_file):
    file_format = get_file_format(basename(path_to_file))
    match file_format:
        case 'json':
            return json.load(open(path_to_file))
        case 'yaml' | 'yml':
            return yaml.load(open(path_to_file), Loader=SafeLoader)
        case _:
            print('Unknown format')
            return None


def get_file_format(file_name):
    for i, char in enumerate(file_name[::-1]):
        if char == '.':
            return file_name[-i::]
    else:
        return None


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
