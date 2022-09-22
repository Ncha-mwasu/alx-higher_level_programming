#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

arg_len = len(argv)
for n in range(0, arg_len):
    count = n
print("{} {}:".format(count, argv[count]))
for n in argv:
    args = n
print("{}: {}".format(count, args))
