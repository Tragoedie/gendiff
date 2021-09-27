from tests.fixtures.result_for_testing import NESTED_STRUCTURE, PLAIN_STRUCTURE
from gendiff.formatters.formatter_stylish import formatter_stylish, get_status, converted, check
from gendiff.formatters.formatter_plain import formatter_plain, converted_plain, path_value
from tests.fixtures.dict_for_testing import DICTIONARY_FOR_TEST
from gendiff.constants import ADDED, DELETED, UNCHANGED


def test_formatter_stylish():
    assert formatter_stylish(DICTIONARY_FOR_TEST) == NESTED_STRUCTURE


def test_stylish_get_status():
    assert get_status(DELETED) == '  - '
    assert get_status(ADDED) == '  + '
    assert get_status(UNCHANGED) == '    '


def test_converted():
    assert converted(False) == 'false'
    assert converted(True) == 'true'
    assert converted(None) == 'null'


def test_check():
    assert check({}) is True
    assert check([]) is False


def test_generate_plain():
    assert formatter_plain(DICTIONARY_FOR_TEST) == PLAIN_STRUCTURE


def test_converted_plain():
    assert converted_plain(False) == 'false'
    assert converted_plain(True) == 'true'
    assert converted_plain(None) == 'null'
    assert converted_plain([]) == '[complex value]'
    assert converted_plain({}) == '[complex value]'


def test_path_value():
    assert path_value('common.', 'key') == 'common.key'
    assert path_value('common.', 'common.') == 'common.'

