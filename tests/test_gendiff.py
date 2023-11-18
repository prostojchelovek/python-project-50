from gendiff.logics.file_comparison import generate_diff
from pathlib import Path


def get_path(file_name):
    p = Path(__file__)
    current_dir = p.absolute().parent
    return str(current_dir / 'fixtures' / file_name)


def test_diff_json():
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    expected = get_path('expected_stylish_json.txt')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()


def test_diff_yaml():
    file1 = get_path('file1.yaml')
    file2 = get_path('file2.yaml')
    expected = get_path('expected_stylish_yaml.txt')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()


def test_diff_yml():
    file1 = get_path('file1.yml')
    file2 = get_path('file2.yml')
    expected = get_path('expected_stylish_yml.txt')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()


def test_diff_deep_json():
    file1 = get_path('deep_file1.json')
    file2 = get_path('deep_file2.json')
    expected = get_path('expected_deep')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()


def test_diff_deep_yaml():
    file1 = get_path('deep_file1.yaml')
    file2 = get_path('deep_file2.yaml')
    expected = get_path('expected_deep')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()


def test_diff_plain_for_deep():
    file1 = get_path('deep_file1.yaml')
    file2 = get_path('deep_file2.yaml')
    expected = get_path('expected_plain_for_deep.txt')
    result = generate_diff(file1, file2, 'plain')
    assert result == open(expected).read()


def test_diff_plain_for_flat():
    file1 = get_path('file1.yaml')
    file2 = get_path('file2.yaml')
    expected = get_path('expected_plain_for_flat.txt')
    result = generate_diff(file1, file2, 'plain')
    assert result == open(expected).read()


def test_diff_json_format():
    file1 = get_path('deep_file1.json')
    file2 = get_path('deep_file2.json')
    expected = get_path('expected_json_format.json')
    result = generate_diff(file1, file2, 'json')
    assert result == open(expected).read()


def test_diff_deep_json():
    file1 = get_path('deep_file3.json')
    file2 = get_path('deep_file4.json')
    expected = get_path('expected_stylish')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()


def test_diff_deep_yml():
    file1 = get_path('deep_file3.json')
    file2 = get_path('deep_file4.json')
    expected = get_path('expected_stylish')
    result = generate_diff(file1, file2)
    assert result == open(expected).read()
