#!/usr/bin/python3

    import hidden_4
    built = dir(hidden_4)
    for name in built:
        if name[:2] != "__":
            print(name)
