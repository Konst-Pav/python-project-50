def get_stylish_output(diff):

    def walk_list(arg_list, offset=0):
        replacer = '  '

        def walk_dict(arg_dict):
            children = arg_dict.get('children')
            if children:
                return f"{replacer * (offset + 2)}{arg_dict['key']}: " + f"{walk_list(children, offset + 2)}"
            else:
                value = transform_dict(arg_dict.get('value'), offset, replacer)
                value1 = transform_dict(arg_dict.get('value1'), offset, replacer)
                value2 = transform_dict(arg_dict.get('value2'), offset, replacer)
                status = arg_dict.get('status')
                if status == 'removed':
                    return f"{replacer * (offset + 1)}- {arg_dict['key']}: {value1}"
                elif status == 'added':
                    return f"{replacer * (offset + 1)}+ {arg_dict['key']}: {value2}"
                elif status == 'updated':
                    return [f"{replacer * (offset + 1)}- {arg_dict['key']}: {value1}",
                            f"{replacer * (offset + 1)}+ {arg_dict['key']}: {value2}"]
                elif status == 'without changes':
                    return f"{replacer * (offset + 1)}  {arg_dict['key']}: {value}"

        return '{\n' + '\n'.join(flatten(list(map(walk_dict, arg_list)))) + '\n' + f"{replacer * offset}" + '}'

    return walk_list(diff)


def transform_dict(value, offset, replacer='  '):
    if isinstance(value, dict):
        result = ['{']
        for key in value:
            inner_value = value[key]
            if isinstance(inner_value, dict):
                result.append(
                    f"{replacer * (offset + 4)}{key}: {transform_dict(inner_value, offset + 2)}")
            else:
                result.append(f"{replacer * (offset + 4)}{key}: {inner_value}")
        result.append(f"{replacer * (offset + 2)}" + '}')
        return '\n'.join(result)
    match value:
        case True | False:
            return str(value).lower()
        case value if value is None:
            return 'null'
        case _:
            return value


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
