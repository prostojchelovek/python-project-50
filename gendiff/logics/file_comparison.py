import math

from gendiff import files_reading
from gendiff.logics.format.plain import plain
from gendiff.logics.format.deep import stylish


# flake8: noqa: C901
def different(data1, data2, status=''):
    result = {}
    if not isinstance(data1, dict) or not isinstance(data2, dict):
        return status

    keys = sorted(list(data1.keys() | data2.keys()))

    for k in keys:
        result[k] = different_helper(data1, data2, k)

    return result


def different_helper(data1, data2, key):
    if key not in data1:
        return different(data1.get(key, -math.inf), data2.get(key, math.inf), 'added')
    elif key not in data2:
        return different(data1.get(key, -math.inf), data2.get(key, math.inf), 'deleted')
    elif data1[key] == data2[key]:
        return different(data1.get(key, -math.inf), data2.get(key, math.inf), 'unchanged')
    else:
        return different(data1.get(key, -math.inf), data2.get(key, math.inf), 'changed')


def generate_diff(file1, file2, format='stylish'):
    data1 = files_reading(file1)
    data2 = files_reading(file2)
    if format == 'stylish':
        return stylish(different(data1, data2), data1, data2)
    elif format == 'plain':
        return plain(different(data1, data2), data1, data2)
