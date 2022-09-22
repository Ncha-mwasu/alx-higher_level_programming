#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
arg_count = len(argv) - 1
if arg_count == 0:
    print("{} arguments.".format(arg_count))
else:
    print("{} arguments:".format(arg_count))
for count in range(arg_count):
    print("{}: {}".format(count + 1, argv[count + 1]))
