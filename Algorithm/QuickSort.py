#!/usr/bin/python

#
# 2016/2/19
# Quick Sort
#


def swap(var1, var2):
    return var2, var1


def quick_sort(data, left, right):
    if left < right:
        pivot = data[left]
        i = left + 1
        j = right
        while True:
            while True:
                if pivot < data[i]:
                    break
                if i == right:
                    break
                i += 1

            while True:
                if pivot >= data[j]:
                    break
                if j == left:
                    break
                j -= 1

            if i < j:
                data[i], data[j] = swap(data[i], data[j])

            if i >= j:
                data[left], data[j] = swap(data[left], data[j])
                break

        quick_sort(data, left, j)
        quick_sort(data, j+1, right)
