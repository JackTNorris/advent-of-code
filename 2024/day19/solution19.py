import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy


def part1():
    can_make = set()
    cant_make = set()
    patterns, to_make = aoc_utils.return_array_from_file('./input.txt')
    patterns = set(patterns[0].split(', '))
    res = 0

    def can_make_design(des: str) -> bool:
        if des in can_make:
            return True
        if des in cant_make:
            return False
        for p in patterns:
            if des == p:
                can_make.add(des)
                return True
            if des.startswith(p):
                if can_make_design(des[len(p):]):
                    can_make.add(des)
                    return True
                else:
                    cant_make.add(des)
        return False

    for t in to_make:
        if can_make_design(t):
            res += 1
    return res

# not 216225835082872685
def part2():
    cant_make = set()
    patterns, to_make = aoc_utils.return_array_from_file('./input.txt')
    patterns = set(patterns[0].split(', '))
    res = 0
    num_ways = defaultdict(lambda: 0)
    def num_ways_to_make(des: str) -> bool:
        ways = 0
        if des in cant_make:
            return 0
        if des in num_ways:
            return num_ways[des]
        for p in patterns:
            if des == p:
                ways += 1
            elif des.startswith(p):
                temp = num_ways_to_make(des[len(p):])
                ways += temp
        if ways == 0:
            cant_make.add(des)
        num_ways[des] = ways
        return ways

    for t in to_make:
        g = num_ways_to_make(t)
        res += g
        print(t + ": ", g)
    return res

print(part2())