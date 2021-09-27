"""This is string formatter."""
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


def formatter_plain(format_dict):
    """Convert format_dict to plain format.

    Parameters:
        format_dict(dict): dict of difference.

    Returns:
        result string.
    """
    result_string = ''

    def for_plain(simple_dict, path_to_next_values, string):
        for key in sorted(simple_dict.keys()):
            path = path_value(path_to_next_values, key)
            if simple_dict[key].get(CONDITION) == ADDED:
                string += "Property '{0}' was added with value: {1}\n".format(
                    path,
                    converted_plain(simple_dict[key][VALUE]),
                )
            elif simple_dict[key].get(CONDITION) == DELETED:
                string += "Property '{0}' was removed\n".format(path)
            elif simple_dict[key].get(CONDITION) == CHANGED:
                string += "Property '{0}' was updated. From {1} to {2}\n".format(
                    path,
                    converted_plain(simple_dict[key][VALUE][OLD_VALUE]),
                    converted_plain(simple_dict[key][VALUE][NEW_VALUE]),
                )
            elif simple_dict[key].get(CONDITION) == UNCHANGED:
                continue
            else:
                string += for_plain(simple_dict[key][VALUE], path + '.', '')
        return string

    for key in sorted(format_dict.keys()):
        path_to_value = key
        if format_dict[key][CONDITION] == NESTED:
            result_string += for_plain(
                format_dict[key][VALUE],
                path_to_value + '.',
                '',
            )
        else:
            result_string += for_plain(
                {key: format_dict[key]},
                path_to_value,
                '',
            )

    return result_string[:len(result_string) - 1]


def converted_plain(value):
    """Editing values.

    Parameters:
        value: name of values.

    Returns:
        new values.
    """
    if isinstance(value, bool):
        return (str(value)).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (dict, list)):
        return '[complex value]'
    return "'{0}'".format(value)


def path_value(path, key):
    """Editing path for string.

    Parameters:
        path: path for key.
        key: ending key.

    Returns:
        new path
    """
    if path == key:
        return path
    return path + key
