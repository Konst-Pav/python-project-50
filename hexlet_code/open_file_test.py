#!/usr/bin/env python3
import json


def open_file(path):
    dict_from_json = json.load(open(path))
    print(dict_from_json)


open_file('/home/konstantin/projects/python-project-50/tests/file_1.json')
