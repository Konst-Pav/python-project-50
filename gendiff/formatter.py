from gendiff.stylish_formatter import stylish_output
from gendiff.plain_formatter import plain_output
from gendiff.json_formatter import json_output


def format_diff(diff, formatter_name):
    match formatter_name:
        case 'stylish':
            return stylish_output(diff)
        case 'plain':
            return plain_output(diff)
        case 'json':
            return json_output(diff)
        case _:
            return stylish_output(diff)
