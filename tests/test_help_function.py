"""Test help function for gendiff."""
from gendiff.constants import ADDED, DELETED, UNCHANGED
from gendiff.formatters.formatter_plain import converted_plain, path_value
from gendiff.formatters.formatter_stylish import converted, get_status


def test_stylish_get_status():  # noqa: D103
    assert get_status(DELETED) == '  - '
    assert get_status(ADDED) == '  + '
    assert get_status(UNCHANGED) == '    '


def test_converted():  # noqa: D103
    assert converted(False) == 'false'
    assert converted(True) == 'true'
    assert converted(None) == 'null'


def test_converted_plain():  # noqa: D103
    assert converted_plain(False) == 'false'
    assert converted_plain(True) == 'true'
    assert converted_plain(None) == 'null'
    assert converted_plain([]) == '[complex value]'
    assert converted_plain({}) == '[complex value]'


def test_path_value():
    assert path_value('common.', 'key') == 'common.key'
    assert path_value('common.', 'common.') == 'common.'
