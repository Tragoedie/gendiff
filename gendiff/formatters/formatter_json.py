"""This is json formatter."""
import json


def formatter_json(format_dict):
    """Convert format_dict to json format.

    Parameters:
        format_dict(format_dict): dict of difference.

    Returns:
        result json file.
    """
    return json.dumps(format_dict, indent=2, sort_keys=True)
