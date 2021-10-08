"""Test generate diff with difference formats."""
import pytest
from gendiff.constants import JSON, PLAIN, STYLISH
from gendiff.gendiff_engine import generate_diff


@pytest.mark.parametrize('path1, path2, formatter, path_to_result', [
    ('tests/fixtures/files/simple_file_before.json',
     'tests/fixtures/files/simple_file_after.json',
     STYLISH,
     'tests/fixtures/results/simple_string.txt',
     ),
    ('tests/fixtures/files/simple_file_before.yaml',
     'tests/fixtures/files/simple_file_after.yaml',
     STYLISH,
     'tests/fixtures/results/simple_string.txt',
     ),
    ('tests/fixtures/files/nested_structure_before.json',
     'tests/fixtures/files/nested_structure_after.json',
     STYLISH,
     'tests/fixtures/results/nested_structure.txt',
     ),
    ('tests/fixtures/files/nested_structure_before.yaml',
     'tests/fixtures/files/nested_structure_after.yaml',
     STYLISH,
     'tests/fixtures/results/nested_structure.txt',
     ),
    ('tests/fixtures/files/nested_structure_before.json',
     'tests/fixtures/files/nested_structure_after.json',
     PLAIN,
     'tests/fixtures/results/plain_structure.txt',
     ),
    ('tests/fixtures/files/nested_structure_before.yaml',
     'tests/fixtures/files/nested_structure_after.yaml',
     PLAIN,
     'tests/fixtures/results/plain_structure.txt',
     ),
    ('tests/fixtures/files/nested_structure_before.json',
     'tests/fixtures/files/nested_structure_after.json',
     JSON,
     'tests/fixtures/results/json_structure.txt',
     ),
    ('tests/fixtures/files/nested_structure_before.yaml',
     'tests/fixtures/files/nested_structure_after.yaml',
     JSON,
     'tests/fixtures/results/json_structure.txt',
     ),
])
def test_formatters(path1, path2, formatter, path_to_result):  # noqa: D103
    assert generate_diff(
        path1,
        path2,
        formatter,
    ) == open_result_file(path_to_result)


def open_result_file(path_to_result):  # noqa: D103
    with open(path_to_result) as file_result:
        result = file_result.read()
    return result
