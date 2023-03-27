#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        while my_list[printed] and printed < x:
            print(my_list[printed], end=" ")
            printed += 1
    except:
        pass
    print()
    return printed
