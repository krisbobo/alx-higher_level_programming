#!/usr/bin/python3
""" Program that Load, add, save all arguments to a Python list,
and then save them to a file """
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    data = "add_item.json"

    if os.path.isfile(data):
        my_list = load_from_json_file(data)
    else:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, data)
