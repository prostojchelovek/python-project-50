from gendiff.logics.format.deep import deep_get_value, type_conversion


# flake8: noqa: C901
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


def return_val_dict(val):
    if not isinstance(val, dict):
        if isinstance(val, str):
            return f"'{val}'"
        return f"{val}"
    return '[complex value]'
