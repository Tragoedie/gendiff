"""Test help function for gendiff."""
from gendiff.constants import ADDED, DELETED, UNCHANGED
from gendiff.formatters.formatter_plain import converting_plain, get_path
from gendiff.formatters.formatter_stylish import (
    converting_stylish,
    get_key_prefix,
)


def test_stylish_get_status():  # noqa: D103
    assert get_key_prefix(DELETED) == '  - '
    assert get_key_prefix(ADDED) == '  + '
    assert get_key_prefix(UNCHANGED) == '    '


def test_converted():  # noqa: D103
    assert converting_stylish(False) == 'false'
    assert converting_stylish(True) == 'true'
    assert converting_stylish(None) == 'null'


def test_converted_plain():  # noqa: D103
    assert converting_plain(False) == 'false'
    assert converting_plain(True) == 'true'
    assert converting_plain(None) == 'null'
    assert converting_plain([]) == '[complex value]'
    assert converting_plain({}) == '[complex value]'


def test_path_value():
    assert get_path('common.', 'key') == 'common.key'
    assert get_path('common.', 'common.') == 'common.'
