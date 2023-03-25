import json
import yaml
from yaml.loader import SafeLoader
from os.path import basename


def convert_to_dict(path_to_file):
    if basename(path_to_file).endswith('json'):
        return json.load(open(path_to_file))
    if basename(path_to_file).endswith(('yaml', 'yml')):
        return yaml.load(open(path_to_file), Loader=SafeLoader)
    else:
        print('Unknown format')
