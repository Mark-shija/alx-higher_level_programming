#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]

    # Replace the element at the specified index if the index is valid
    if 0 <= idx < len(my_list):
        new_list[idx] = element

    return new_list
