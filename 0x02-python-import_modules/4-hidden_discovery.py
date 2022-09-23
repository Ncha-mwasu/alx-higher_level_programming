#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    builtins = dir(hidden_4)

    list_len = len(builtins)
    for items in range(0, list_len):
        num = builtins[items]
        if num[:2] != '__':
            print(num)
