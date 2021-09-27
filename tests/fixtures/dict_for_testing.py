DICTIONARY_FOR_TEST = {'common': {
    'condition': 'nested', 'value': {
        'setting1': {'condition': 'unchanged', 'value': 'Value 1'},
        'setting2': {'condition': 'deleted', 'value': 200},
        'setting3': {'condition': 'changed', 'value': {'old_value': True, 'new_value': None}},
        'setting6': {'condition': 'nested', 'value': {
            'key': {'condition': 'unchanged', 'value': 'value'},
            'ops': {'condition': 'added', 'value': 'vops'}}},
        'follow': {'condition': 'added', 'value': False},
        'setting4': {'condition': 'added', 'value': 'blah blah'},
        'setting5': {'condition': 'added', 'value': {'key5': 'value5'}}
    }
},
    'group1': {'condition': 'nested', 'value': {
        'baz': {'condition': 'changed', 'value': {'old_value': 'bas', 'new_value': 'bars'}},
        'foo': {'condition': 'unchanged', 'value': 'bar'},
        'nest': {'condition': 'changed', 'value': {'old_value': {'key': 'value'}, 'new_value': 'str'}}
    }
},
    'group2': {'condition': 'deleted', 'value': {'abc': 12345, 'deep': {'id': 45}}},
    'group3': {'condition': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
}
