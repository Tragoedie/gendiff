"""This is the difference logic."""
from gendiff.parser_file import parser_file


def generate_diff(file_path1, file_path2):
    """Get difference two file.

    Args:
        file_path1 (string): Path to the first file.
        file_path2 (string): Path to the second file.

    Returns:
         basestring: difference.
    """
    first_file = parser_file(file_path1, file_path1[file_path1.rfind('.'):])
    second_file = parser_file(file_path2, file_path2[file_path2.rfind('.'):])
    diff_result = ['{\n']
    for key_file1, value_file1 in first_file.items():
        if second_file.get(key_file1) is None:
            diff_result.append('  - {0}: {1}\n'.format(key_file1, value_file1))
        elif first_file.get(key_file1) == second_file.get(key_file1):
            diff_result.append('    {0}: {1}\n'.format(key_file1, value_file1))
        else:
            diff_result.append(
                '  - {0}: {1}\n  + {2}: {3}\n'.format
                (key_file1, value_file1, key_file1, second_file[key_file1]),
            )
    for key_file2, value_file2 in second_file.items():
        if first_file.get(key_file2) is None:
            diff_result.append('  + {0}: {1}\n'.format(key_file2, value_file2))
    diff_result.sort(key=lambda name: name[3:])
    diff_result.append('}')
    return ''.join(diff_result)
