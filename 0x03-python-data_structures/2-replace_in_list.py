#!/usr/bin/python3
""" Functionthat replace element in a list using index"""


def replace_in_list(my_list, idx, new_element):
    list_len = len(my_list) - 1
    if (idx < 0 or idx > list_len):
        return (my_list)
    else:
        my_list[idx] = new_element
        return (my_list)
