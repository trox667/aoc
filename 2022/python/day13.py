#!/usr/bin/python3

from itertools import zip_longest
import functools
import math


def match_type(left, right):
    if type(left) is list and type(right) is int:
        return (left, [right])
    elif type(left) is int and type(right) is list:
        return ([left], right)
    else:
        return left, right


RIGHT_ORDER, EQUAL, WRONG_ORDER = -1, 0, 1


def compare(left, right):
    if right == None:
        return WRONG_ORDER
    elif left == None:
        return RIGHT_ORDER

    if type(left) == type(right) == int:
        if left < right:
            return RIGHT_ORDER
        elif left > right:
            return WRONG_ORDER
        else:
            return EQUAL

    elif type(left) == type(right) == list:
        for left, right in zip_longest(left, right, fillvalue=None):
            result = compare(left, right)
            if result != EQUAL:
                return result
        return EQUAL

    left, right = match_type(left, right)
    return compare(left, right)


with open('../inputs/input13') as f:
    pairs = [[eval(p) for p in pairs.split('\n')]
             for pairs in f.read().split('\n\n')]
    print('Part 1:', sum(
        [i + 1 for i, r in enumerate([compare(p[0], p[1]) for p in pairs]) if r == RIGHT_ORDER]))

    items = [[[2]], [[6]]] + [item for pair in pairs for item in pair]
    items = sorted(items, key=functools.cmp_to_key(compare))
    print('Part 2:', math.prod(
        ([i + 1 for i, item in enumerate(items) if item == [[2]] or item == [[6]]])))
