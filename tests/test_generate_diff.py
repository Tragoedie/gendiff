from gendiff.gendiff_engine import generate_diff
from tests.fixtures.result_for_testing import SIMPLE_STRING


def test_generate_diff_json():
    assert generate_diff('./tests/fixtures/simple_file_before.json',
                         './tests/fixtures/simple_file_after.json')\
           == SIMPLE_STRING


def test_generate_diff_yaml():
    assert generate_diff('./tests/fixtures/simple_file_before.yaml',
                         './tests/fixtures/simple_file_after.yaml') \
           == SIMPLE_STRING

