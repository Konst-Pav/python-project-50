def get_plain_output(diff):

    def walk_list(arg_list, path=[]):

        def walk_dict(arg_dict):
            key = arg_dict['key']
            new_path = [*path, key]
            children = arg_dict.get('children')
            if children:
                return walk_list(children, new_path)
            status = arg_dict.get('status')

            def add_formatting(value):
                if isinstance(value, dict):
                    return '[complex value]'
                if isinstance(value, bool):
                    return str(value).lower()
                if value is None:
                    return 'null'
                if isinstance(value, str):
                    return f"\'{value}\'"
                else:
                    return value

            value1 = add_formatting(arg_dict.get('value1'))
            value2 = add_formatting(arg_dict.get('value2'))
            full_path = '.'.join(new_path)

            match status:
                case 'added':
                    return f"Property \'{full_path}\' was added with value: {value2}"
                case 'removed':
                    return f"Property \'{full_path}\' was removed"
                case 'updated':
                    return f"Property \'{full_path}\' was updated. From {value1} to {value2}"
                case _:
                    return ''

        return '\n'.join(list(filter(None, map(walk_dict, arg_list))))

    return walk_list(diff)
