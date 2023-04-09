import json
import os
os.chdir(os.path.dirname(__file__))


def get_notes_from_json():
    with open("data/notes.json", "r", encoding="utf-8") as f:
        notes = json.load(f)
    return notes

def write_notes_to_json(notes):
    with open("data/notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f)

def table(headers, data):
    lens = {}
    for key, value in headers.items():
        lens[key] = 0
    for item in data:
        for key, value in headers.items():
            if len(item[key]) > lens[key]:
                lens[key] = len(item[key])
    res = "+"
    for key, value in headers.items():
        if lens[key] < len(value):
            lens[key] = len(value) + 1
        res += f"{' ' * (lens[key] - len(value) - 1)}{value} +"
    res += "\n|"
    for key, value in headers.items():
        res += f"{'-' * lens[key]}|"
    res += "\n"
    for item in data:
        temp = "|"
        for key, value in headers.items():
            temp += f"{' ' * (lens[key] - len(item[key]))}{item[key]}|"
        res += temp
        res += "\n"
    res += "+"
    for key, value in headers.items():
        res += f"{'-' * lens[key]}+"
    return res

