import json


def get_json_output(diff):
    return json.dumps(diff, sort_keys=True, indent=4)
