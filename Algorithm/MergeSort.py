#!/usr/bin/python


def merge_sort(data, result_array):
    if len(data) > 1:
        right_array = []
        left_array = []
        result_right_array = []
        result_left_array = []
        middle = len(data) / 2

        for i in range(middle):
            left_array.append(data[i])

        for i in range(middle, len(data)):
            right_array.append(data[i])

        merge_sort(left_array, result_left_array)
        merge_sort(right_array, result_right_array)

        merge(result_left_array, result_right_array, result_array)
    else:
        result_array.append(data.pop())


def merge(left_array, right_array, result_array):
    left_index = 0
    right_index = 0
    left_len = len(left_array)
    right_len = len(right_array)

    for i in range(left_len + right_len):
        if left_index == left_len:
            result_array.append(right_array[right_index])
            right_index += 1
        elif right_index == right_len:
            result_array.append(left_array[left_index])
            left_index += 1
        elif left_array[left_index] >= right_array[right_index]:
            result_array.append(right_array[right_index])
            right_index += 1
        elif left_array[left_index] < right_array[right_index]:
            result_array.append(left_array[left_index])
            left_index += 1