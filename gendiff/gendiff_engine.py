"""This is the difference logic."""
from gendiff.constants import (
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    NESTED,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGED,
    VALUE,
)
from gendiff.formatters.formatter_plain import formatter_plain
from gendiff.formatters.formatter_stylish import formatter_stylish
from gendiff.parser_file import parser_file


def generate_diff(file_path1, file_path2, formatter_name='stylish'):
    """Get difference two file.

    Args:
        file_path1 (string): Path to the first file.
        file_path2 (string): Path to the second file.
        formatter_name (string): 'stylish'

    Returns:
         basestring: difference.
    """
    first_file = parser_file(file_path1, file_path1[file_path1.rfind('.'):])
    second_file = parser_file(file_path2, file_path2[file_path2.rfind('.'):])
    difference_diff = {}

    def gen_diff(first_dict, second_dict, diff_diff):
        for key in first_dict:
            if key not in second_dict:
                diff_diff[key] = {CONDITION: DELETED, VALUE: first_dict[key]}
            elif first_dict.get(key) == second_dict.get(key):
                diff_diff[key] = {CONDITION: UNCHANGED, VALUE: first_dict[key]}
            else:
                if isinstance(second_dict.get(key), dict):
                    diff_diff[key] = {
                        CONDITION: NESTED,
                        VALUE: gen_diff(
                            first_dict[key],
                            second_dict[key],
                            {},
                        ),
                    }
                else:
                    diff_diff[key] = {
                        CONDITION: CHANGED,
                        VALUE: {
                            OLD_VALUE: first_dict[key],
                            NEW_VALUE: second_dict[key],
                        },
                    }
        for key_s in second_dict:
            if first_dict.get(key_s) is None:
                diff_diff[key_s] = {CONDITION: ADDED, VALUE: second_dict[key_s]}
        return diff_diff

    return _select_formatter(formatter_name)(
        gen_diff(first_file, second_file, difference_diff),
    )


def _select_formatter(formatter_name):
    """Select formatter for output format.

    Parameters:
        formatter_name: name of output format name.

    Returns:
        output format
    """
    formatters = {
        'stylish': formatter_stylish,
        'plain': formatter_plain,
    }
    return formatters[formatter_name]
