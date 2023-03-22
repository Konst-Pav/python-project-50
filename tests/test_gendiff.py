#!/usr/bin/env python3
from gendiff_util.gendiff import generate_diff, sorted_unique_keys, convert_to_dict, stylish, plain
from tests.fixtures.diff_nested_struct import diff_nested_struct_to_tests as diff_nested_struct
from tests.fixtures.stylish_fixture_test import stylish_fixture
from tests.fixtures.plain_fixture_test import plain_fixture

json_file1 = './tests/fixtures/file_1.json'
json_file2 = './tests/fixtures/file_2.json'
yaml_file1 = './tests/fixtures/file_1.yml'
yaml_file2 = './tests/fixtures/file_2.yml'
nested_struct_file1 = './tests/fixtures/file_3.json'
nested_struct_file2 = './tests/fixtures/file_4.json'

stylish_test_file1 = './tests/fixtures/nested_struct_1.json'
stylish_test_file2 = './tests/fixtures/nested_struct_2.json'

plane_struct_diff = [{'key': 'follow', 'value1': False, 'status': 'removed'},
                     {'key': 'host', 'value': 'hexlet.io', 'status': 'without changes'},
                     {'key': 'proxy', 'value1': '123.234.53.22', 'status': 'removed'},
                     {'key': 'timeout', 'value1': 50, 'value2': 20, 'status': 'updated'},
                     {'key': 'verbose', 'value2': True, 'status': 'added'}]

plane_dict1 = {'key': 'value', 'car': 'bmw'}
plane_dict2 = {'key': 'value', 'games': 'starcraft'}

nested_dict1 = {'key': {'nested_key': 'value'}}
nested_dict2 = {'key': {'nested_key': 'value'}}


converted_file = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}


def test_generate_diff_in_plane_struct():
    assert generate_diff(json_file1, json_file2) == plane_struct_diff
    assert generate_diff(yaml_file1, yaml_file2) == plane_struct_diff


def test_generate_diff_in_nested_struct():
    assert generate_diff(nested_struct_file1, nested_struct_file2) == diff_nested_struct


def test_get_sorted_unique_keys():
    assert sorted_unique_keys(plane_dict1, plane_dict2) == ['car', 'games', 'key']


def test_convert_json_to_dict():
    assert convert_to_dict(json_file1) == converted_file


def test_convert_yaml_to_dict():
    assert convert_to_dict(yaml_file1) == converted_file


def test_stylish_formatter():
    assert stylish(generate_diff(stylish_test_file1, stylish_test_file2)) == str(stylish_fixture)


def test_plain_formatter():
    print(plain(generate_diff(stylish_test_file1, stylish_test_file2)))
    assert plain(generate_diff(stylish_test_file1, stylish_test_file2)) == str(plain_fixture)
