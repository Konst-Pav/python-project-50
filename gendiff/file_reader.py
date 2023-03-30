import json
import yaml
from yaml.loader import SafeLoader
from os.path import basename


def get_dict_from_file(path_to_file):
    file = read_file(path_to_file)
    file_format = get_file_format(path_to_file)
    if file_format == 'json':
        return json.load(file)
    elif file_format == 'yaml':
        return yaml.load(file, Loader=SafeLoader)
    else:
        print('Unknown format. The following formats are available: json, yaml, yml.')


def get_file_format(file_name):
    if basename(file_name).endswith('json'):
        return 'json'
    elif basename(file_name).endswith(('yaml', 'yml')):
        return 'yaml'
    else:
        return None


def read_file(path_to_file):
    return open(path_to_file)
