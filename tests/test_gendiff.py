#!/usr/bin/env python3
from gendiff.scripts.gendiff import generate_diff
from gendiff.parser import parse_data
from tests.fixtures.diff_nested_struct import diff_nested_struct_to_tests as diff_nested_struct
from tests.fixtures.stylish_fixture_test import stylish_fixture
from tests.fixtures.plain_fixture_test import plain_fixture

json_file1 = './tests/fixtures/file_1.json'
json_file2 = './tests/fixtures/file_2.json'
yaml_file1 = './tests/fixtures/file_1.yml'
yaml_file2 = './tests/fixtures/file_2.yml'
nested_struct_file1 = './tests/fixtures/file_3.json'
nested_struct_file2 = './tests/fixtures/file_4.json'

nested_struct_file3 = './tests/fixtures/nested_struct_1.json'
nested_struct_file4 = './tests/fixtures/nested_struct_2.json'

plane_struct_diff = [{'key': 'follow', 'value1': False, 'status': 'removed'},
                     {'key': 'host', 'value': 'hexlet.io', 'status': 'without changes'},
                     {'key': 'proxy', 'value1': '123.234.53.22', 'status': 'removed'},
                     {'key': 'timeout', 'value1': 50, 'value2': 20, 'status': 'updated'},
                     {'key': 'verbose', 'value2': True, 'status': 'added'}]


def test_parse_data_plane_struct():
    assert parse_data(json_file1, json_file2) == plane_struct_diff
    assert parse_data(yaml_file1, yaml_file2) == plane_struct_diff


def test_parse_data_nested_struct():
    assert parse_data(nested_struct_file1, nested_struct_file2) == diff_nested_struct


def test_stylish_formatter():
    assert generate_diff(nested_struct_file3, nested_struct_file4, 'stylish') == stylish_fixture


def test_plain_formatter():
    assert generate_diff(nested_struct_file3, nested_struct_file4, 'plain') == plain_fixture
