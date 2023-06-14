#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0
    for elmt in my_list:
        avg += (elmt[0] * elmt[1])
        size += elmt[1]
    return (avg / size)
