from gendiff.scripts.gendiff import generate_diff
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return current_dir / 'fixtures' / file_name


def test_diff():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    expected = get_path('expected.txt')

    assert generate_diff(file1, file2) == open(expected).read()
