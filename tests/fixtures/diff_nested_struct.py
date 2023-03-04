diff_nested_struct_to_tests = [
    {'key': 'common', 'children': [
        {'key': 'follow', 'conclusion': 'Added', 'value': {'before': None, 'after': False}},
        {'key': 'setting1', 'conclusion': 'Same', 'value': {'before': 'Value 1', 'after': 'Value 1'}},
        {'key': 'setting2', 'conclusion': 'Removed', 'value': {'before': 200, 'after': None}},
        {'key': 'setting3', 'conclusion': 'Removed', 'value': {'before': True, 'after': None}},
        {'key': 'setting4', 'conclusion': 'Added', 'value': {'before': None, 'after': 'blah blah'}},
        {'key': 'setting5', 'conclusion': 'Added', 'value': {'before': None, 'after': {'key5': 'value5'}}},
        {'key': 'setting6', 'children': [
            {'key': 'doge', 'children': [
                {'key': 'wow', 'conclusion': 'Changed', 'value': {'before': '', 'after': 'so much'}}]},
            {'key': 'key', 'conclusion': 'Same', 'value': {'before': 'value', 'after': 'value'}},
            {'key': 'ops', 'conclusion': 'Added', 'value': {'before': None, 'after': 'vops'}}]}]},
    {'key': 'group1', 'children': [
        {'key': 'baz', 'conclusion': 'Changed', 'value': {'before': 'bas', 'after': 'bars'}},
        {'key': 'foo', 'conclusion': 'Same', 'value': {'before': 'bar', 'after': 'bar'}},
        {'key': 'nest', 'conclusion': 'Changed', 'value': {'before': {'key': 'value'}, 'after': 'str'}}]},
    {'key': 'group2', 'conclusion': 'Removed', 'value': {'before': {'abc': 12345, 'deep': {'id': 45}}, 'after': None}},
    {'key': 'group3', 'conclusion': 'Added', 'value': {'before': None, 'after': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}]
