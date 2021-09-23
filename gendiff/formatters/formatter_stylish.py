"""This is string formatter."""
from gendiff.constants import ADDED, CONDITION, DELETED, UNCHANGED, VALUE


def formatter_stylish(format_dict):
    """Convert format_dict to string.

    Parameters:
        format_dict(dict): dict of difference.

    Returns:
        result string.
    """
    tabs = ''

    def form(simple_dict, tab, string):
        for key in sorted(simple_dict.keys()):
            if check(simple_dict[key]) and simple_dict[key].get(VALUE) is None:
                string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                    tab,
                    get_status(simple_dict[key].get(CONDITION)),
                    key,
                    form(simple_dict[key], tab + '    ', ''),
                )
            elif check(simple_dict[key]) and check(simple_dict[key][VALUE]):
                if 'old_value' in simple_dict[key][VALUE]:
                    if isinstance(simple_dict[key][VALUE]['old_value'], dict):
                        string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                            tab,
                            get_status(DELETED),
                            key,
                            form(
                                simple_dict[key][VALUE]['old_value'],
                                tab + '    ',
                                '',
                            ),
                        )
                    else:
                        string += '{0}{1}{2}: {3}\n'.format(
                            tab,
                            get_status(DELETED),
                            key,
                            converted(simple_dict[key][VALUE]['old_value']),
                        )
                    if isinstance(simple_dict[key][VALUE]['new_value'], dict):
                        string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                            tab,
                            get_status(ADDED),
                            key,
                            form(
                                simple_dict[key][VALUE]['new_value'],
                                tab + '    ',
                                '',
                            ),
                        )
                    else:
                        string += '{0}{1}{2}: {3}\n'.format(
                            tab,
                            get_status(ADDED),
                            key,
                            converted(simple_dict[key][VALUE]['new_value']),
                        )
                else:
                    string += '{0}{1}{2}: {{\n{3}{0}    }}\n'.format(
                        tab,
                        get_status(simple_dict[key].get(CONDITION)),
                        key,
                        form(simple_dict[key][VALUE], tab + '    ', ''),
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

    return '{{\n{0}}}'.format(form(format_dict, tabs, ''))


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
        new values
    """
    if value is False:
        return 'false'
    elif value is True:
        return 'true'
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
