import itertools

from functools import reduce


# flake8: noqa: C901
def stylish(value, data1, data2):
    replacer = ' '
    spaces_count = 4

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


def deep_get_value(dictionary, path):
    return reduce(dict.get, path, dictionary)


def type_conversion(data):
    edit_data_false = data.replace('False', 'false')
    edit_data_true = edit_data_false.replace('True', 'true')
    edit_data = edit_data_true.replace('None', 'null')
    return edit_data

