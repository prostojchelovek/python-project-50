from gendiff import files_reading


def generate_diff(file1, file2):
    result = ''
    input1, input2 = files_reading(file1), files_reading(file2)
    set_keys1, set_keys2 = set(input1), set(input2)
    only_in_file1 = set_keys1.difference(set_keys2)
    only_in_file2 = set_keys2.difference(set_keys1)
    file_intersection = set_keys1.intersection(set_keys2)
    all_keys = sorted(list(set_keys1.union(set_keys2)))
    for elem in all_keys:
        if elem in only_in_file1:
            result += f"  - {elem}: {input1[elem]}\n"
        elif elem in only_in_file2:
            result += f"  + {elem}: {input2[elem]}\n"
        elif elem in file_intersection and input1[elem] == input2[elem]:
            result += f"    {elem}: {input1[elem]}\n"
        else:
            result += (f"  - {elem}: {input1[elem]}\n"
                       f"  + {elem}: {input2[elem]}\n")
    return '{\n' + result + '}\n'
