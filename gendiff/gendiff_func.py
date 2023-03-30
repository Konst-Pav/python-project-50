#!/usr/bin/env python3
from gendiff.parser import parse_files
from gendiff.formatters.formatter import format_diff


def generate_diff(path_to_file1, path_to_file2, formatter_name='stylish'):
    return format_diff(parse_files(path_to_file1, path_to_file2), formatter_name)
