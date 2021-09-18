"""Read sourse module."""

import json

import yaml


def parser_file(input_file, type_of_file):
    """Parse input_file into a dict.

    Args:
        input_file (path to file): input data.
        type_of_file (str): input data format.

    Returns:
         dict: dictionary of data.
    """
    if type_of_file == '.json':
        with open(input_file) as json_file:
            data_file = json.load(json_file)
    elif type_of_file in {'.yaml', '.yml'}:
        with open(input_file) as yaml_file:
            data_file = yaml.safe_load(yaml_file)
    else:
        return -1
    return data_file
