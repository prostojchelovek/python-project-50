import itertools
import math

from functools import reduce
from gendiff import files_reading


# flake8: noqa: C901
def stylish(value, data1, data2, replacer=' ', spaces_count=4):

    def iter_(current_value, depth, keys):
        if not isinstance(current_value, dict):
            return f"{current_value}"

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []

        for key, val in current_value.items():
            keys.append(key)
            if val == 'added':
                val1 = deep_get_value(data2, keys)
                lines.append(f'{deep_indent[2:]}+ {key}: '
                             f'{iter_(val1, deep_indent_size, keys)}'.rstrip())
            elif val == 'deleted':
                val2 = deep_get_value(data1, keys)
                lines.append(f'{deep_indent[2:]}- {key}: '
                             f'{iter_(val2, deep_indent_size, keys)}'.rstrip())
            elif val == 'changed':
                val1 = deep_get_value(data1, keys)
                lines.append(f'{deep_indent[2:]}- {key}: '
                             f'{iter_(val1, deep_indent_size, keys)}'.rstrip())
                val2 = deep_get_value(data2, keys)
                lines.append(f'{deep_indent[2:]}+ {key}: '
                             f'{iter_(val2, deep_indent_size, keys)}'.rstrip())
            elif val == 'unchanged':
                val1 = deep_get_value(data1, keys)
                lines.append(f'{deep_indent[2:]}  {key}: '
                             f'{iter_(val1, deep_indent_size, keys)}'.rstrip())
            else:
                lines.append(f'{deep_indent[2:]}  {key}: '
                             f'{iter_(val, deep_indent_size, keys)}'.rstrip())
            keys.pop()
        result = itertools.chain("{", lines, [current_indent + "}"])
        return type_conversion('\n'.join(result))

    return iter_(value, 0, [])


def plain(value, data1, data2):
    lines = []

    def iter_(current_value, keys):
        if not isinstance(current_value, dict):
            return f"{current_value}"

        for key, val in current_value.items():
            keys.append(key)
            if val == 'added':
                val2 = deep_get_value(data2, keys)
                lines.append(f"Property '{'.'.join(keys)}' "
                             f"was added with value: {return_val_dict(val2)}")
            elif val == 'deleted':
                lines.append(f"Property '{'.'.join(keys)}' "
                             f"was removed")
            elif val == 'changed':
                val1 = deep_get_value(data1, keys)
                val2 = deep_get_value(data2, keys)
                lines.append(f"Property '{'.'.join(keys)}'"
                             f" was updated. From {return_val_dict(val1)}"
                             f" to {return_val_dict(val2)}")
            elif val != 'unchanged':
                iter_(val, keys)
            keys.pop()
        return type_conversion('\n'.join(lines))

    return iter_(value, [])


# flake8: noqa: C901
def different(data1, data2, status=''):
    result = {}
    if not isinstance(data1, dict) or not isinstance(data2, dict):
        return status
    for key, value in data1.items():
        if isinstance(value, dict) and data2.get(key, math.inf) != math.inf:
            different(data1[key], data2[key])
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


def type_conversion(data):
    edit_data_false = data.replace('False', 'false')
    edit_data_true = edit_data_false.replace('True', 'true')
    edit_data = edit_data_true.replace('None', 'null')
    return edit_data


def return_val_dict(val):
    if not isinstance(val, dict):
        if isinstance(val, str):
            return f"'{val}'"
        return f"{val}"
    return '[complex value]'


def generate_diff(file1, file2, format='stylish'):
    data1 = files_reading(file1)
    data2 = files_reading(file2)
    if format == 'stylish':
        return stylish(different(data1, data2), data1, data2)
    elif format == 'plain':
        return plain(different(data1, data2), data1, data2)


def deep_get_value(dictionary, path):
    return reduce(dict.get, path, dictionary)
