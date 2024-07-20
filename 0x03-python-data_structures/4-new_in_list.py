def new_in_list(my_list, idx, element):
    # Check if index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    
    # a copy of the original list
    new_list = my_list[:]
    
    new_list[idx] = element 
    return new_list
