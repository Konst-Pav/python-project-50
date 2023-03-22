diff_nested_struct_to_tests = [
    {'key': 'games', 'children': [
        {'key': 'rpg', 'children': [
            {'key': '3dpv', 'value1': 'hades', 'value2': 'conan', 'status': 'updated'},
            {'key': 'fpv', 'value1': 'fallout', 'status': 'removed'}
        ]},
        {'key': 'sim', 'value2': 'il2', 'status': 'added'},
        {'key': 'strategy', 'value1': 'wc3', 'value2': 'sc2', 'status': 'updated'}
    ]},
    {'key': 'num', 'value': 123, 'status': 'without changes'}
]

dict1 = {
    'num': 123,
    'games': {
        'strategy': 'wc3',
        'rpg': {
            'fpv': 'fallout',
            '3dpv': 'hades'
        }
    }
}

dict2 = {
    'num': 123,
    'games': {
        'sim': 'il2',
        'strategy': 'sc2',
        'rpg': {
            '3dpv': 'conan'
        }
    }
}


diff = [
    {'key': 'common', 'children': [
        {'key': 'setting1', 'value': 'Value 1', 'status': 'without changes'},
        {'key': 'setting2', 'value': 200, 'status': 'without changes'},
        {'key': 'setting3', 'value': True, 'status': 'without changes'},
        {'key': 'setting6', 'children': [
            {'key': 'doge', 'children': [
                {'key': 'wow', 'value': '', 'status': 'without changes'}]},
            {'key': 'key', 'value': 'value', 'status': 'without changes'}]}]},
    {'key': 'group1', 'children': [
        {'key': 'baz', 'value': 'bas', 'status': 'without changes'},
        {'key': 'foo', 'value': 'bar', 'status': 'without changes'},
        {'key': 'nest', 'children': [
            {'key': 'key', 'value': 'value', 'status': 'without changes'}]}]},
    {'key': 'group2', 'children': [
        {'key': 'abc', 'value': 12345, 'status': 'without changes'},
        {'key': 'deep', 'children': [
            {'key': 'id', 'value': 45, 'status': 'without changes'}]}]}]
