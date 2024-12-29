import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy
from functools import cmp_to_key
import numpy as np

def evaluate(expression, graph):
    n1, op, n2 = expression.split(' ')
    if op == 'AND':
        return graph[n1] and graph[n2]
    if op == 'OR': 
        return graph[n1] or graph[n2]
    if op == 'XOR':
        return graph[n1] ^ graph[n2]
    raise Exception("Invalid operation")


def part1():
    data = aoc_utils.return_array_from_file('input.txt')
    locks = []
    keys = []
    # sort locks and keys
    for item in data:
        numerical_representation = np.zeros(5)
        for i in range(len(item)):
            numerical_representation += np.array(list(map(lambda x: 1 if x == '#' else 0, item[i])))
        if item[0] == "#####":
            locks.append((numerical_representation - 1))
        else:
            keys.append((numerical_representation - 1))

    res = 0
    for key in keys:
        for lock in locks:
            if max(key + lock) < 6:
                res += 1
    return res

print("Part 1: ", part1())
    