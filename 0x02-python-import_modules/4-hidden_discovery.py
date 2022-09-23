#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4
    builtins = dir(hidden_4)
    for items in builtins:
        if items[:2] != "__":
            print(items)
