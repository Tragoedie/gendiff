from gendiff.gendiff_engine import generate_diff
from tests.fixtures.result_gendiff_json import string_result


def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json',
                         './tests/fixtures/file2.json')\
           == string_result
