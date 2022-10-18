#!/usr/bin/python3
"""
A module full name computation module
"""


def say_my_name(first_name, last_name=""):
    """This function computes one's full name using two strings
    Args:
        first_name: first string
        last_name: second string

        Return:
            full name: a string concatenation of first and last name

        Raises:
            TypeError: If first_name and/or last_name is/are not of string type
    """

    if not isinstance(first_name, str) or not first_name:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    else:
        if last_name == "":
            print(f"My name is {first_name}")

        else:
            print(f"My name is {first_name} {last_name}")
