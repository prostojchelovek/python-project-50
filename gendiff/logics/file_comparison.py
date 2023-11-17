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
        if k not in data1:
            result[k] = different(data1.get(k, -math.inf),
                                  data2.get(k, math.inf), 'added')
        elif k not in data2:
            result[k] = different(data1.get(k, -math.inf),
                                  data2.get(k, math.inf), 'deleted')
        elif data1[k] == data2[k]:
            result[k] = different(data1.get(k, -math.inf),
                                  data2.get(k, math.inf), 'unchanged')
        else:
            result[k] = different(data1.get(k, -math.inf),
                                  data2.get(k, math.inf), 'changed')
    return result


def generate_diff(file1, file2, format='stylish'):
    data1 = files_reading(file1)
    data2 = files_reading(file2)
    if format == 'stylish':
        return stylish(different(data1, data2), data1, data2)
    elif format == 'plain':
        return plain(different(data1, data2), data1, data2)
