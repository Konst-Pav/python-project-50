from gendiff.formatters.stylish_formatter import get_stylish_output
from gendiff.formatters.plain_formatter import get_plain_output
from gendiff.formatters.json_formatter import get_json_output


def format_diff(diff, formatter_name):
    match formatter_name:
        case 'stylish':
            return get_stylish_output(diff)
        case 'plain':
            return get_plain_output(diff)
        case 'json':
            return get_json_output(diff)
        case _:
            return 'Unknown format. The following formats are available: "stylish", "plain", "json".'
