#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_len = len(argv)
    Sum = 0

    for args in range(1, arg_len):
        Sum += int(argv[args])
    print("{}".format(Sum))
