#!/usr/bin/python3
"""
Function to write to a file
"""


def read_file(filename=""):
    """
    Writing to a file
    """

    with open(filename, encoding = 'utf-8') as f:
        f.read()
