#!/usr/bin/env python3
import argparse
import json
import yaml
from yaml.loader import SafeLoader
from os.path import basename


def generate_diff(file1, file2):
    dict_before = convert_to_dict(file1)
    dict_after = convert_to_dict(file2)

    def get_list_of_diff(arg_dict1, arg_dict2):
        unique_keys = sorted_unique_keys(arg_dict1, arg_dict2)

        def compare_values(key):

            def no_such_key(): pass
            value1 = arg_dict1.get(key, no_such_key)
            value2 = arg_dict2.get(key, no_such_key)
            diff = {'key': key}
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff.update({'children': get_list_of_diff(value1, value2)})
            else:
                if value1 == no_such_key and value2 != no_such_key:
                    diff.update({'value2': value2, 'status': 'added'})
                elif value2 == no_such_key and value1 != no_such_key:
                    diff.update({'value1': value1, 'status': 'removed'})
                elif value1 != value2:
                    diff.update({'value1': value1, 'value2': value2, 'status': 'updated'})
                else:
                    diff.update({'value': value1, 'status': 'without changes'})
            return diff

        return flatten(list(map(compare_values, unique_keys)))
    return get_list_of_diff(dict_before, dict_after)


def sorted_unique_keys(arg_dict, *args):
    unique_keys = set(arg_dict.keys())
    for item in args:
        unique_keys.update(item.keys())
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


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)

    walk(tree)
    return result


def stylish(diff):

    def flatten(tree):
        result = []

        def walk(subtree):
            for item in subtree:
                if isinstance(item, list):
                    walk(item)
                else:
                    result.append(item)

        walk(tree)
        return result

    def walk_list(arg_list, offset=0):
        dots = '  '

        def walk_dict(arg_dict):
            children = arg_dict.get('children')
            if children:
                return f"{dots * (offset + 2)}{arg_dict['key']}: " + f"{walk_list(children, offset + 2)}"
            else:

                def transform_value(value, offset):
                    if isinstance(value, dict):
                        result = ['{']
                        for key in value:
                            inner_value = value[key]
                            if isinstance(inner_value, dict):
                                result.append(
                                    f"{dots * (offset + 4)}{key}: {transform_value(inner_value, offset + 2)}")
                            else:
                                result.append(f"{dots * (offset + 4)}{key}: {inner_value}")
                        result.append(f"{dots * (offset + 2)}" + '}')
                        return '\n'.join(result)
                    else:
                        match value:
                            case True | False:
                                return str(value).lower()
                            case value if value is None:
                                return 'null'
                            case _:
                                return value
                value = transform_value(arg_dict.get('value'), offset)
                value1 = transform_value(arg_dict.get('value1'), offset)
                value2 = transform_value(arg_dict.get('value2'), offset)
                status = arg_dict.get('status')
                if status == 'removed':
                    return f"{dots * (offset + 1)}- {arg_dict['key']}: {value1}".rstrip()
                elif status == 'added':
                    return f"{dots * (offset + 1)}+ {arg_dict['key']}: {value2}".rstrip()
                elif status == 'updated':
                    return [f"{dots * (offset + 1)}- {arg_dict['key']}: {value1}".rstrip(),
                            f"{dots * (offset + 1)}+ {arg_dict['key']}: {value2}".rstrip()]
                elif status == 'without changes':
                    return f"{dots * (offset + 1)}  {arg_dict['key']}: {value}".rstrip()

        return '{\n' + '\n'.join(flatten(list(map(walk_dict, arg_list)))) + '\n' + f"{dots * offset}" + '}'

    return walk_list(diff)


def plain(diff):

    def walk_list(arg_list, path=[]):

        def walk_dict(arg_dict):
            key = arg_dict['key']
            new_path = [*path, key]
            children = arg_dict.get('children')
            if children:
                return walk_list(children, new_path)
            status = arg_dict.get('status')

            def add_formatting(value):
                if isinstance(value, dict):
                    return '[complex value]'
                if isinstance(value, bool):
                    return str(value).lower()
                if value is None:
                    return 'null'
                if isinstance(value, str):
                    return f"\'{value}\'"
                else:
                    return value

            value1 = add_formatting(arg_dict.get('value1'))
            value2 = add_formatting(arg_dict.get('value2'))
            full_path = '.'.join(new_path)

            match status:
                case 'added':
                    return f"Property \'{full_path}\' was added with value: {value2}"
                case 'removed':
                    return f"Property \'{full_path}\' was removed"
                case 'updated':
                    return f"Property \'{full_path}\' was updated. From {value1} to {value2}"
                case _:
                    return ''

        return '\n'.join(list(filter(None, map(walk_dict, arg_list))))

    return walk_list(diff)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
