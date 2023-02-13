#!/usr/bin/env python3
from hexlet_code.gendiff import generate_diff


file1 = './tests/file_1.json'
file2 = './tests/file_2.json'
# file2 = '/home/konstantin/projects/python-project-50/tests/file_2.json'
result = '- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true'


def test_generate_diff():
    assert generate_diff(file1, file2) == result
