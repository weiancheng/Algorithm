#!/usr/bin/python


def test_fibonacci():
    print "fibonacci 7: " + str(fibonacci(8))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)