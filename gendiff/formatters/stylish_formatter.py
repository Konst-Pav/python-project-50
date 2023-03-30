from gendiff.parser import parse_data


def get_stylish_output(diff):

    def walk_list(arg_list, level=0):
        replacer = '  '

        def walk_dict(arg_dict):
            children = arg_dict.get('children')
            status = arg_dict.get('status', '  ')
            offset = (replacer * 2) * level
            if children:
                return f"{offset}{replacer + status}{arg_dict['key']}: " + f"{walk_list(children, level + 1)}"
            value = transform_inner_dict(arg_dict.get('value'))
            value1 = transform_inner_dict(arg_dict.get('value1'))
            value2 = transform_inner_dict(arg_dict.get('value2'))
            if status == 'removed':
                return f"{offset}{replacer}- {arg_dict['key']}: {value1}"
            elif status == 'added':
                return f"{offset}{replacer}+ {arg_dict['key']}: {value2}"
            elif status == 'updated':
                return [f"{offset}{replacer}- {arg_dict['key']}: {value1}",
                        f"{offset}{replacer}+ {arg_dict['key']}: {value2}"]
            elif status == 'without changes':
                return f"{offset}{replacer}  {arg_dict['key']}: {value}"

        def transform_inner_dict(value):
            if isinstance(value, dict):
                return walk_list(parse_data(value, value), level + 1)
            else:
                match value:
                    case True | False:
                        return str(value).lower()
                    case value if value is None:
                        return 'null'
                    case _:
                        return value

        res_list = flatten(list(map(walk_dict, arg_list)))
        result = '\n'.join(res_list)
        return "{\n" + result + "\n" + f"{(replacer * 2) * level}" + "}"

    return walk_list(diff)


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
