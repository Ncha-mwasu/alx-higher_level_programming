#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import __init__, my_secret_santa, print_school, print_hidden
    builtins = dir()
    # print(builtins)
    list_len = len(builtins)
    for items in range(0, list_len):
        num = builtins[items]
        if num[:2] != '__':
            num = builtins[items]
            print(num)
