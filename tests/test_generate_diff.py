from gendiff.gendiff_engine import generate_diff
from tests.fixtures.result_gendiff_json import string_result


def test_generate_diff():
    assert generate_diff('/media/tragoedia/TEMP/python_1/hexlet/python-project-lvl2/tests/fixtures/file1.json',
                         '/media/tragoedia/TEMP/python_1/hexlet/python-project-lvl2/tests/fixtures/file2.json')\
           == string_result
