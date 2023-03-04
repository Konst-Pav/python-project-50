#!/usr/bin/env python3
from hexlet_code.gendiff import generate_diff, get_sorted_unique_keys, convert_to_dict
from tests.fixtures.diff_nested_struct import diff_nested_struct_to_tests as diff_nested_struct


json_file1 = './tests/fixtures/file_1.json'
json_file2 = './tests/fixtures/file_2.json'
json_file3 = './tests/fixtures/file_3.json'
json_file4 = './tests/fixtures/file_4.json'
nested_struct_file1 = './tests/fixtures/nested_struct_1.json'
nested_struct_file2 = './tests/fixtures/nested_struct_2.json'

yaml_file1 = './tests/fixtures/file_1.yml'
yaml_file2 = './tests/fixtures/file_2.yml'
# file2 = '/home/konstantin/projects/python-project-50/tests/file_2.json'


# Без изменений ' '      Same
# Изменилось    '-' '+'  Changed
# Удалено       '-'      Removed
# Добавлено     '+'      Added

plane_result = [{'conclusion': 'Removed', 'key': 'follow', 'value': {'before': False, 'after': None}},
                {'conclusion': 'Same', 'key': 'host', 'value': {'before': 'hexlet.io', 'after': 'hexlet.io'}},
                {'conclusion': 'Removed', 'key': 'proxy', 'value': {'before': '123.234.53.22', 'after': None}},
                {'conclusion': 'Changed', 'key': 'timeout', 'value': {'before': 50, 'after': 20}},
                {'conclusion': 'Added', 'key': 'verbose', 'value': {'before': None, 'after': True}}]

plane_dict1 = {'key': 'value', 'car': 'bmw'}
plane_dict2 = {'key': 'value', 'games': 'starcraft'}

nested_dict1 = {'key': {'nested_key': 'value'}}
nested_dict2 = {'key': {'nested_key': 'value'}}

# Без изменений ' '      Same
# Изменилось    '-' '+'  Changed
# Удалено       '-'      Removed
# Добавлено     '+'      Added

nested_result = [{'conclusion': 'Same', 'key': 'key1', 'value': {'before': 'value1', 'after': 'value1'}},
                 {'conclusion': 'Added', 'key': 'key2', 'value': {'before': None, 'after': 'value2'}},
                 {'conclusion': ' ', 'key': 'nested-struct', 'value': [
                    {'conclusion': 'Same', 'key': 'nested-key2', 'value': {'before': 'value2', 'after': 'value2'}},
                    {'conclusion': 'Added', 'key': 'nested-key3', 'value': {'before': None, 'after': 'value3'}}]
                 }]

converted_file = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}


def test_generate_diff_in_plane_struct():
    assert generate_diff(json_file1, json_file2) == plane_result
    assert generate_diff(yaml_file1, yaml_file2) == plane_result


def test_generate_diff_in_nested_struct():
    assert generate_diff(nested_struct_file1, nested_struct_file2) == diff_nested_struct


def test_get_sorted_unique_keys():
    assert get_sorted_unique_keys(plane_dict1, plane_dict2) == ['car', 'games', 'key']


def test_convert_json_to_dict():
    assert convert_to_dict(json_file1) == converted_file


def test_convert_yaml_to_dict():
    assert convert_to_dict(yaml_file1) == converted_file
