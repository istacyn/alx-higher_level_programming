#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list): A list of unsorted integers.

    Returns:
        int or None: The peak element found in the list
        or None if the list is empty or no peak is found.
    """
    length = len(list_of_integers)
    mid_element = length
    mid = length // 2

    if length == 0:
        return None

    while True:
        mid_element = mid_element // 2
        if (mid < length - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_element // 2 == 0:
                mid_element = 2
            mid = mid + mid_element // 2
        elif mid_element > 0 and \
                list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_element // 2 == 0:
                mid_element = 2
            mid = mid - mid_element // 2
        else:
            return list_of_integers[mid]
