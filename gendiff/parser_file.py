"""Read sourse module."""

import json

import yaml


def parser_file(path_to_file):
    """Parse input_file into a dict.

    Args:
        path_to_file (path to file): input data.

    Returns:
         dict: dictionary of data.

    Raises:
        ValueError: if format of file is unsupported.
    """
    type_of_file = path_to_file[path_to_file.rfind('.'):].lower()
    if type_of_file == '.json':
        with open(path_to_file) as json_file:
            return json.load(json_file)
    elif type_of_file in {'.yaml', '.yml'}:
        with open(path_to_file) as yaml_file:
            return yaml.safe_load(yaml_file)
    raise ValueError('Unsupported file format')
