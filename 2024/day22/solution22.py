import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy


def mix(secret, gv):
    return secret ^ gv

def prune(secret):
    return secret % 16777216

def get_next_secret_number(secret):
    res = secret * 64
    secret = prune(mix(secret, res))
    res = int(secret / 32)
    secret = prune(mix(secret, res))
    res = secret * 2048
    secret = prune(mix(secret, res))
    return secret

def part1():
    data = aoc_utils.return_array_from_file('input.txt')[0]
    res = 0
    for item in data:
        secret = int(item)
        for i in range(2000):
            secret = get_next_secret_number(secret)
        res += secret
    return res

print(part1())