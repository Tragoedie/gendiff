from gendiff.gendiff_engine import generate_diff
from tests.fixtures.result_for_testing import SIMPLE_STRING, NESTED_STRUCTURE, PLAIN_STRUCTURE, JSON_STRUCTURE


def test_generate_diff_simple_json():
    assert generate_diff('./tests/fixtures/simple_file_before.json',
                         './tests/fixtures/simple_file_after.json')\
           == SIMPLE_STRING


def test_generate_diff_simple_yaml():
    assert generate_diff('./tests/fixtures/simple_file_before.yaml',
                         './tests/fixtures/simple_file_after.yaml') \
           == SIMPLE_STRING


def test_generate_stylish_json():
    assert generate_diff('./tests/fixtures/nested_structure_before.json',
                         './tests/fixtures/nested_structure_after.json') \
           == NESTED_STRUCTURE


def test_generate_stylish_yaml():
    assert generate_diff('./tests/fixtures/nested_structure_before.yaml',
                         './tests/fixtures/nested_structure_after.yaml') \
           == NESTED_STRUCTURE


def test_generate_plain_json():
    assert generate_diff('./tests/fixtures/nested_structure_before.json',
                         './tests/fixtures/nested_structure_after.json', 'plain') \
           == PLAIN_STRUCTURE


def test_generate_plain_yaml():
    assert generate_diff('./tests/fixtures/nested_structure_before.yaml',
                         './tests/fixtures/nested_structure_after.yaml', 'plain') \
           == PLAIN_STRUCTURE


def test_generate_json():
    assert generate_diff('./tests/fixtures/nested_structure_before.json',
                         './tests/fixtures/nested_structure_after.json', 'json') \
           == JSON_STRUCTURE


def test_generate_yaml():
    assert generate_diff('./tests/fixtures/nested_structure_before.yaml',
                         './tests/fixtures/nested_structure_after.yaml', 'json') \
           == JSON_STRUCTURE
