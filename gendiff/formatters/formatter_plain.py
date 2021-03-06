"""This is string formatter."""
from gendiff.constants import (  # noqa: WPS235
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    NESTED,
    UNCHANGED,
    VALUE,
)


def formatter_plain(diff_structure):  # noqa: WPS231, WPS221, C901
    """Convert format_dict to plain format.

    Parameters:
        diff_structure(dict): dict of difference.

    Returns:
        result string.
    """
    result_string = []
    return '\n'.join(_for_plain(diff_structure, '', result_string))


def _for_plain(diff, path_prefix, string):  # noqa: WPS231, WPS221, C901
    for key in sorted(diff.keys()):
        path = get_path(path_prefix, key)
        if diff[key].get(CONDITION) == ADDED:
            string.append("Property '{0}' was added with value: {1}".format(
                path,
                converting_plain(diff[key][VALUE]),
            ))
        elif diff[key].get(CONDITION) == DELETED:
            string.append("Property '{0}' was removed".format(path))
        elif diff[key].get(CONDITION) == CHANGED:
            string.append("Property '{0}' was updated. From {1} to {2}".format(
                path,
                converting_plain(diff[key][VALUE][DELETED]),
                converting_plain(diff[key][VALUE][ADDED]),
            ))
        elif diff[key].get(CONDITION) == UNCHANGED:
            continue
        elif diff[key].get(CONDITION) == NESTED:
            string += _for_plain(diff[key][VALUE], path + '.', [])
    return string


def converting_plain(value):
    if isinstance(value, bool):
        value = (str(value)).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, (dict, list)):
        value = '[complex value]'
    elif isinstance(value, str):
        value = "'{0}'".format(value)
    return value


def get_path(path, key):
    if path == key:
        return path
    return path + key
