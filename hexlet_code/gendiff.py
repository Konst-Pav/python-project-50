#!/usr/bin/env python3
import argparse
import json


def generate_diff(file_path_1, file_path_2):
    # Приведение к dict
    file1 = json.load(open(file_path_1))
    file2 = json.load(open(file_path_2))
    # Сравнение двух dict
    # Множество всех ключей
    all_keys = set()
    all_keys.update(file1.keys())
    all_keys.update(file2.keys())
    # Сортировка ключей
    all_keys = list(all_keys)
    all_keys.sort()
    # Сравниваем соответственно условиям
    result = []
    for key in all_keys:
        result.append(compare_by_key(key, file1, file2))
    return '\n'.join(result)


def compare_by_key(key, first_dict, second_dict):
    first_value = first_dict.get(key)
    second_value = second_dict.get(key)
    # Исправляем bool
    if isinstance(first_value, bool):
        first_value = str(first_value).lower()
    if isinstance(second_value, bool):
        second_value = str(second_value).lower()
    #
    match (first_value, second_value):
        case (first_value, None):
            return f'- {key}: {first_value}'
        case (None, second_value):
            return f'+ {key}: {second_value}'
        case (first_value, second_value) if first_value == second_value:
            return f'  {key}: {first_value}'
        case (first_value, second_value) if first_value != second_value:
            return f'- {key}: {first_value}\n+ {key}: {second_value}'
        case _:
            print('Something went wrong')


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
