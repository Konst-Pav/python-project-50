#!/usr/bin/env python3
import argparse
import json


def json_to_dict(json_file):
    return json.load(json_file)


def yml_to_dict(yml_file):
    return


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
    match key:
        # Есть в первом файле, нет во втором
        case 1 if first_value is not None and second_value is None:
            print('Igogo')
            return f'- {key}: {first_value}'
        # Есть во втором файле, нет в первом
        case 2 if second_value is not None and first_value is None:
            return f'+ {key}: {second_value}'
        # Значения идентичны
        case 3 if first_value == second_value:
            return f'  {key}: {first_value}'
        # Значения различны
        case 4 if first_value != second_value:
            return f'- {key}: {first_value}\n+ {key}: {second_value}'
        case _:
            print(f'Hello! {key} {first_value}, {second_value}')


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
