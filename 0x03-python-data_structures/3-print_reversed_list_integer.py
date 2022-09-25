    #!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    new_list = my_list
    list_len = len(new_list) - 1
    for items in new_list:
        print("{}".format(items))
