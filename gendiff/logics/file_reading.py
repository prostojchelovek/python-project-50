import json
import yaml


def files_reading(file):
    if file.lower().endswith('.json'):
        return json.load(open(file))
    elif file.lower().endswith(('.yaml', 'yml')):
        return yaml.full_load(open(file))
    else:
        return "Incorrect file format"
