import sys, os
import numpy as np
from collections import defaultdict
sys.path.append('../../')
import aoc_utils

def part1():
    rules, updates = aoc_utils.return_array_from_file('./input.txt')
    rules_map = defaultdict(lambda: set())
    for rule in rules:
        b, a = list(map(lambda x: int(x), rule.split('|')))
        rules_map[b].add(a)
    sum = 0
    for update in updates:
        temp = list(map(lambda x: int(x), update.split(',')))
        update_set = set(temp)
        valid_flag = True
        for num in temp:
            if num in rules_map.keys():
                for n in rules_map[num]:
                    if n in update_set:
                        if temp.index(n) < temp.index(num):
                            valid_flag = False
                            break
            if not valid_flag:
                break
        if valid_flag:
            sum += temp[int(len(temp) / 2)]
    return sum

print("Part1: ", part1())