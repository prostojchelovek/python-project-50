import json
import yaml


def files_reading(file1, file2):
    if file1.lower().endswith('.json') and file2.lower().endswith('.json'):
        return json.load(open(file1)), json.load(open(file2))
    elif (file1.lower().endswith(('.yaml', 'yml'))
          and file2.lower().endswith(('.yaml', 'yml'))):
        return yaml.full_load(open(file1)), yaml.full_load(open(file2))
    else:
        return "Incorrect file format or different formats"
