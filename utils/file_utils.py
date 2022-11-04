import json
import os.path


def get_file_contents(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            file_contents = json.load(f)
            return file_contents
    else:
        raise FileNotFoundError
