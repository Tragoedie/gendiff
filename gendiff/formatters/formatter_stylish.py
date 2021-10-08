"""This is string formatter."""
from gendiff.constants import (
    ADDED,
    CONDITION,
    DELETED,
    NEW_VALUE,
    OLD_VALUE,
    UNCHANGED,
    VALUE,
)


def formatter_stylish(format_dict):  # noqa: WPS231, WPS221, C901
    """Convert format_dict to string format.

    Parameters:
        format_dict(dict): dict of difference.

    Returns:
        result string.
    """
    tabs = ''
    result_string = '{{\n{0}}}'.format(_form(format_dict, tabs, ''))
    return result_string.strip()


def _form(simple_dict, tab, string):  # noqa: WPS231, WPS221, C901
    for key in sorted(simple_dict.keys()):
        if check(simple_dict[key]) and VALUE not in simple_dict[key]:
            string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                tab,
                get_status(simple_dict[key].get(CONDITION)),
                key,
                _form(simple_dict[key], tab + '    ', ''),
            )
        elif check(simple_dict[key]) and check(simple_dict[key][VALUE]):
            if 'old_value' in simple_dict[key][VALUE]:
                if isinstance(simple_dict[key][VALUE][OLD_VALUE], dict):
                    string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                        tab,
                        get_status(DELETED),
                        key,
                        _form(
                            simple_dict[key][VALUE][OLD_VALUE],
                            tab + '    ',
                            '',
                        ),
                    )
                else:
                    string += '{0}{1}{2}: {3}\n'.format(
                        tab,
                        get_status(DELETED),
                        key,
                        converted(simple_dict[key][VALUE][OLD_VALUE]),
                    )
                if isinstance(simple_dict[key][VALUE][NEW_VALUE], dict):
                    string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                        tab,
                        get_status(ADDED),
                        key,
                        _form(
                            simple_dict[key][VALUE][NEW_VALUE],
                            tab + '    ',
                            '',
                        ),
                    )
                else:
                    string += '{0}{1}{2}: {3}\n'.format(
                        tab,
                        get_status(ADDED),
                        key,
                        converted(simple_dict[key][VALUE][NEW_VALUE]),
                    )
            else:
                string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                    tab,
                    get_status(simple_dict[key].get(CONDITION)),
                    key,
                    _form(simple_dict[key][VALUE], tab + '    ', ''),
                )
        else:
            if isinstance(simple_dict[key], dict):
                value = simple_dict[key][VALUE]
                cond = simple_dict[key].get(CONDITION)
            else:
                value = simple_dict[key]
                cond = UNCHANGED
            string += '{0}{1}{2}: {3}\n'.format(
                tab,
                get_status(cond),
                key,
                converted(value),
            )
    return string


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


def check(value):
    """Check if dictionary.

    Parameters:
        value: checked value.

    Returns:
        boolean: is dictionary
    """
    return isinstance(value, dict)
