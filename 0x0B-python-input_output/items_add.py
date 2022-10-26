#!/usr/bin/python3
"""
A sys module
"""
from sys import argv

if __name__=="__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        content = load_json("add_item.json")
    except FileNotFoundError:
        content = []
    finally:
        content.extend(argv[1:])
        save_json(content, "add_item.json")
