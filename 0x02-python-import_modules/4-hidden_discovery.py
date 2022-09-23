#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import __init__, my_secret_santa, print_school, print_hidden
    builtins = dir()
    list_len = len(builtins)
    for items in range(0, list_len):
        if items > 9:
            print(builtins[items])
