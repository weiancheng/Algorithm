#!/usr/bin/python

def binary_search(input_list, value):
    lowest = 0
    highest = len(input_list) - 1

    while lowest <= highest:
        mid = (lowest + highest) / 2
        if input_list[mid] == value:
            return mid
        elif input_list[mid] < value:
            lowest = mid + 1
        elif input_list[mid] > value:
            highest = mid - 1
    return -1
