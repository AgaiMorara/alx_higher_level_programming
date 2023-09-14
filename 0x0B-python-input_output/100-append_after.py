#!/usr/bin/python3
"""
module writes a function that inserts a line of text to a file, after
each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ implementation, just uses string in another and getlines as a list
    """

    with open(filename) as f:
        my_list = list(f.readlines())
        for index, line in enumerate(my_list):
            if search_string in line:
                my_list.insert(index + 1, new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(my_list)
