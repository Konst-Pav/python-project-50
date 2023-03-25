import json
import yaml
from yaml.loader import SafeLoader
from os.path import basename


def convert_to_dict(path_to_file):
    file_format = get_file_format(basename(path_to_file))
    match file_format:
        case 'json':
            return json.load(open(path_to_file))
        case 'yaml' | 'yml':
            return yaml.load(open(path_to_file), Loader=SafeLoader)
        case _:
            # TODO: add exception
            print('Unknown format')
            return None


def get_file_format(file_name):
    for i, char in enumerate(file_name[::-1]):
        if char == '.':
            return file_name[-i::]
