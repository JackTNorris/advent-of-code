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

def part2():
    data = aoc_utils.return_array_from_file('input.txt')[0]
    res = 0
    buyer_price_changes = []
    selling_prices = []
    for item in data:
        price_changes = []
        sp = []
        secret = int(item)
        for i in range(2000):
            sp.append(int(str(secret)[-1]))
            temp = secret
            secret = get_next_secret_number(secret)
            price_changes.append(int(str(secret)[-1]) - int(str(temp)[-1]))
        buyer_price_changes.append(price_changes)
        selling_prices.append(sp)

    buyer_maps = [defaultdict(lambda: 0) for i in range(len(data))]
    all_possibilities = set()
    for buyer_index in range(len(buyer_price_changes)):
        for z in range(len(buyer_price_changes[buyer_index]) - 4):
            to_match = buyer_price_changes[buyer_index][z:z+4]
            price = selling_prices[buyer_index][z + 4]
            if tuple(to_match) not in buyer_maps[buyer_index]:
                buyer_maps[buyer_index][tuple(to_match)] = price
                all_possibilities.add(tuple(to_match))
    print('made buyer map')
    res = 0
    for poss in all_possibilities:
        sum = 0
        for i in range(len(buyer_maps)):
            sum += buyer_maps[i][poss]
        res = max(res, sum)
    return res


print("Part 2: ", part2())