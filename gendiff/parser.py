from gendiff.file_reader import convert_to_dict


def parse_files(file1, file2):
    dict_before = convert_to_dict(file1)
    dict_after = convert_to_dict(file2)
    return parse_data(dict_before, dict_after)


def parse_data(arg_dict1, arg_dict2):
    unique_keys = sorted_unique_keys(arg_dict1, arg_dict2)

    def compare_values(key):
        def no_such_key(): pass  # noqa: E704
        value1 = arg_dict1.get(key, no_such_key)
        value2 = arg_dict2.get(key, no_such_key)
        diff = {'key': key}
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff.update({'children': parse_data(value1, value2)})
        else:
            if value1 == no_such_key and value2 != no_such_key:
                diff.update({'value2': value2, 'status': 'added'})
            elif value2 == no_such_key and value1 != no_such_key:
                diff.update({'value1': value1, 'status': 'removed'})
            elif value1 != value2:
                diff.update({'value1': value1, 'value2': value2, 'status': 'updated'})
            else:
                diff.update({'value': value1, 'status': 'without changes'})
        return diff

    return flatten(list(map(compare_values, unique_keys)))


def sorted_unique_keys(arg_dict, *args):
    unique_keys = set(arg_dict.keys())
    for item in args:
        unique_keys.update(item.keys())
    list_unique_keys = list(unique_keys)
    list_unique_keys.sort()
    return list_unique_keys


def flatten(tree):
    result = []

    def walk(subtree):
        for item in subtree:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)

    walk(tree)
    return result
