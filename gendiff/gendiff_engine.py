"""This is the difference logic."""
from gendiff.constants import (  # noqa:WPS235
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    JSON,
    NESTED,
    PLAIN,
    STYLISH,
    UNCHANGED,
    VALUE,
)
from gendiff.formatters.formatter_json import formatter_json
from gendiff.formatters.formatter_plain import formatter_plain
from gendiff.formatters.formatter_stylish import formatter_stylish
from gendiff.parser_file import parse_file


def generate_diff(file_path1, file_path2, formatter_name=STYLISH):
    """Get difference two file.

    Args:
        file_path1 (string): Path to the first file.
        file_path2 (string): Path to the second file.
        formatter_name (string): 'stylish'

    Returns:
         basestring: difference.
    """
    content_one = parse_file(file_path1)
    content_two = parse_file(file_path2)
    return _select_formatter(formatter_name)(
        _gen_diff(content_one, content_two),
    )


def _gen_diff(first_dict, second_dict):  # noqa: C901, WPS231, WPS210, WPS221, E501
    diff_diff = {}
    shared_keys = (first_dict.keys() & second_dict.keys())
    deleted_keys = (first_dict.keys() - second_dict.keys())
    added_keys = (second_dict.keys() - first_dict.keys())
    for key in deleted_keys:
        diff_diff[key] = {CONDITION: DELETED, VALUE: first_dict[key]}
    for key2 in shared_keys:
        if first_dict.get(key2) == second_dict.get(key2):
            diff_diff[key2] = {CONDITION: UNCHANGED, VALUE: first_dict[key2]}
        elif isinstance(second_dict.get(key2), dict) and isinstance(first_dict.get(key2), dict):  # noqa:E501, WPS221
            diff_diff[key2] = {
                CONDITION: NESTED,
                VALUE: _gen_diff(first_dict[key2], second_dict[key2]),
            }
        else:
            diff_diff[key2] = {
                CONDITION: CHANGED,
                VALUE: {
                    DELETED: first_dict[key2],
                    ADDED: second_dict[key2],
                },
            }
    for key3 in added_keys:
        diff_diff[key3] = {CONDITION: ADDED, VALUE: second_dict[key3]}
    return diff_diff


def _select_formatter(formatter_name):
    """Select formatter for output format.

    Parameters:
        formatter_name: name of output format name.

    Returns:
        output format
    """
    formatters = {
        STYLISH: formatter_stylish,
        PLAIN: formatter_plain,
        JSON: formatter_json,
    }
    return formatters[formatter_name]
