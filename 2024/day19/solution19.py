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



print(part1())