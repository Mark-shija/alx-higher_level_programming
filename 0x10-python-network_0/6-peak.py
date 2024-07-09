#!/usr/bin/python3


def find_peak(lst_of_integers):

    if lst_of_integers is None or len(lst_of_integers) == 0:
        return None

    if len(lst_of_integers) == 1:
        return lst_of_integers[0]

    idx = int(len(lst_of_integers) / 2)

    if idx != len(lst_of_integers) - 1:
        if lst_of_integers[idx - 1] < lst_of_integers[idx] and\
           lst_of_integers[idx + 1] < lst_of_integers[idx]:
            return lst_of_integers[idx]
    else:
        if lst_of_integers[idx - 1] < lst_of_integers[idx]:
            return lst_of_integers[idx]
        else:
            return lst_of_integers[idx - 1]

    if lst_of_integers[idx - 1] > lst_of_integers[idx]:
        a_list = lst_of_integers[0:idx]
    else:
        a_list = lst_of_integers[idx + 1:]

    return find_peak(a_list)
