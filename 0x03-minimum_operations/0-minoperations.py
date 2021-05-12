#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ function that's calculate minium operations"""
    if not isinstance(n, int) or n < 2:
        return 0
    operation = 0
    odd = 3

    if n % 2 == 0:
        operation += 2
        n = n//2
    if odd <= n:
        if n % odd == 0:
            operation += odd
            n = n//odd
        odd += 2
    return int(operation)