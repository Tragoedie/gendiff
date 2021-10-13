"""This is string formatter."""
from gendiff.constants import (
    ADDED,
    CHANGED,
    CONDITION,
    DELETED,
    FORMAT_STRING,
    UNCHANGED,
    VALUE,
)


def formatter_stylish(format_dict):
    """Convert format_dict to string format.

    Parameters:
        format_dict(dict): dict of difference.

    Returns:
        result string.
    """
    tabs = ''
    result_string = '{{\n{0}}}'.format(_for_stylish(format_dict, tabs, ''))
    return result_string.strip()


def _for_stylish(simple_dict, tab, string):
    for key in sorted(simple_dict.keys()):
        condition = UNCHANGED
        if isinstance(simple_dict[key], dict):
            condition = simple_dict[key].get(CONDITION)
        if condition == CHANGED:
            string += FORMAT_STRING.format(
                tab,
                get_status(DELETED),
                key,
                get_value(simple_dict[key][VALUE][DELETED], tab + '    '),
            )
            string += FORMAT_STRING.format(
                tab,
                get_status(ADDED),
                key,
                get_value(simple_dict[key][VALUE][ADDED], tab + '    '),
            )
        else:
            string += FORMAT_STRING.format(
                tab,
                get_status(condition),
                key,
                get_value(simple_dict[key], tab + '    '),
            )
    return string


def get_value(data_items, tab):
    """Return value in string format.

    Parameters:
        data_items: value to execute.
        tab: offset

    Returns:
        value string.
    """
    if isinstance(data_items, dict) and VALUE in data_items:
        return get_value(data_items[VALUE], tab)
    elif isinstance(data_items, dict):
        return '{{\n{0}{1}}}'.format(_for_stylish(data_items, tab, ''), tab)
    return converted(data_items)


def get_status(value):
    """Convert name to value.

    Parameters:
        value: name of parameters.

    Returns:
        new value.
    """
    if value == DELETED:
        return '  - '
    elif value == ADDED:
        return '  + '
    return '    '


def converted(value):
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
    return value
