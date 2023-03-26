parse_data_result = [
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

parse_data_dict1 = {
    'num': 123,
    'games': {
        'strategy': 'wc3',
        'rpg': {
            'fpv': 'fallout',
            '3dpv': 'hades'
        }
    }
}

parse_data_dict2 = {
    'num': 123,
    'games': {
        'sim': 'il2',
        'strategy': 'sc2',
        'rpg': {
            '3dpv': 'conan'
        }
    }
}
