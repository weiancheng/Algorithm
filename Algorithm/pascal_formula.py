#!/usr/bin/python


def test_pascal_formula():
    result = pascal_formula()


def pascal_formula(n, k):
    return (n - 1, k) + (n - 1, k - 1)


# n! = n x (n - 1) x (n - 2) x ... x 2 x 1
def factorial(n):
    result = 1
    m = 1
    if n is 0 or n is 1:
        return 1

    while n >= m:
        result *= m
        m += 1

    return result


def permutation(n, r):
    return factorial(n) / factorial(n - r)
