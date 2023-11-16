from gendiff.logics.file_comparison import generate_diff, stylish
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return str(current_dir / 'fixtures' / file_name)


def test_diff_json():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    expected = get_path('expected_json.txt')
    result = stylish(generate_diff(file1, file2), file1, file2)
    assert result == open(expected).read()


def test_diff_yaml():
    file1 = get_path('file1.yaml')
    file2 = get_path('file2.yaml')
    expected = get_path('expected_yaml.txt')
    result = stylish(generate_diff(file1, file2), file1, file2)
    assert result == open(expected).read()


def test_diff_yml():
    file1 = get_path('file1.yml')
    file2 = get_path('file2.yml')
    expected = get_path('expected_yml.txt')
    result = stylish(generate_diff(file1, file2), file1, file2)
    assert result == open(expected).read()


def test_diff_deep_json():
    file1 = get_path('deep_file1.json')
    file2 = get_path('deep_file2.json')
    expected = get_path('expected_deep.txt')
    result = stylish(generate_diff(file1, file2), file1, file2)
    assert result == open(expected).read()


def test_diff_deep_yaml():
    file1 = get_path('deep_file1.yaml')
    file2 = get_path('deep_file2.yaml')
    expected = get_path('expected_deep.txt')
    result = stylish(generate_diff(file1, file2), file1, file2)
    assert result == open(expected).read()
