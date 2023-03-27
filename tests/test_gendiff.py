#!/usr/bin/env python3
import pytest
from gendiff.file_reader import convert_to_dict
from gendiff.scripts.gendiff import generate_diff
from gendiff.parser import parse_data
from tests.fixtures.dict_from_file import convert_to_dict_result
from tests.fixtures.stylish_fixture_test import stylish_fixture
from tests.fixtures.plain_fixture_test import plain_fixture
from tests.fixtures.diff_nested_struct import parse_data_result, parse_data_dict1, parse_data_dict2
from gendiff.gendiff_cli import parse_args

json_file1 = './tests/fixtures/nested_struct_1.json'
json_file2 = './tests/fixtures/nested_struct_2.json'
yaml_file1 = './tests/fixtures/nested_struct_1.yml'
yaml_file2 = './tests/fixtures/nested_struct_2.yml'
stylish_expected_result = stylish_fixture
plain_expected_result = plain_fixture

json_file = './tests/fixtures/file.json'
yaml_file = './tests/fixtures/file.yaml'
yml_file = './tests/fixtures/file.yml'


@pytest.mark.parametrize('file1, file2, formatter_name, expected_result', [
    (json_file1, json_file2, 'stylish', stylish_fixture),
    (yaml_file1, yaml_file2, 'stylish', stylish_fixture),
    (json_file1, json_file2, 'plain', plain_fixture),
    (yaml_file1, yaml_file2, 'plain', plain_fixture),
])
def test_formatter(file1, file2, formatter_name, expected_result):
    result = generate_diff(file1, file2, formatter_name)
    assert result == expected_result


@pytest.mark.parametrize('path_to_file, expected_result', [
    (json_file, convert_to_dict_result),
    (yaml_file, convert_to_dict_result),
    (yml_file, convert_to_dict_result),
])
def test_convert_to_dict(path_to_file, expected_result):
    result = convert_to_dict(path_to_file)
    assert result == expected_result


@pytest.mark.parametrize('dict1, dict2, expected_result', [
    (parse_data_dict1, parse_data_dict2, parse_data_result)
])
def test_parse_data(dict1, dict2, expected_result):
    result = parse_data(dict1, dict2)
    assert result == expected_result


@pytest.mark.parametrize('option, format_name, path_to_file1, path_to_file2, expected_result', [
    ('-f', 'stylish', '~/path/file1', '~/path/file2', ('stylish', '~/path/file1', '~/path/file2'))
])
def test_gendiff_cli(option, format_name, path_to_file1, path_to_file2, expected_result):
    args = parse_args([option, format_name, path_to_file1, path_to_file2])
    result = (args.format, args.first_file, args.second_file)
    assert result == expected_result
