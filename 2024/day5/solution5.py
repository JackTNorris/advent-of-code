import sys, os
import numpy as np
from collections import defaultdict
sys.path.append('../../')
import aoc_utils

def is_valid_update(update, rules_map):
    update_set = set(update)
    valid_flag = True
    for num in update:
        if num in rules_map.keys():
            for n in rules_map[num]:
                if n in update_set:
                    if update.index(n) < update.index(num):
                        valid_flag = False
                        break
        if not valid_flag:
                break
    return valid_flag

def part1():
    rules, updates = aoc_utils.return_array_from_file('./input.txt')
    rules_map = defaultdict(lambda: set())
    for rule in rules:
        b, a = list(map(lambda x: int(x), rule.split('|')))
        rules_map[b].add(a)
    sum = 0
    for update in updates:
        temp = list(map(lambda x: int(x), update.split(',')))
        if is_valid_update(temp, rules_map):
            sum += temp[int(len(temp) / 2)]
    return sum

def part2():
    rules, updates = aoc_utils.return_array_from_file('./input.txt')
    rules_map = defaultdict(lambda: set())
    for rule in rules:
        b, a = list(map(lambda x: int(x), rule.split('|')))
        rules_map[b].add(a)
    bad_updates = []
    for update in updates:
        temp = list(map(lambda x: int(x), update.split(',')))
        if not is_valid_update(temp, rules_map):
            bad_updates.append(temp)

    # assuming there is a correct order, reconstruct it
    def fix_update(b_u):
        new_update = [b_u[0]]
        index = 1
        while len(new_update) < len(b_u) and index < len(b_u):
            for i in range(len(new_update) + 1):
                temp = new_update[::]
                temp.insert(i, b_u[index])
                if is_valid_update(temp, rules_map):
                    new_update.insert(i, b_u[index])
                    break
            index += 1
        return new_update
    new_sum = 0
    for bad_update in bad_updates:
        temp = fix_update(bad_update)
        print("fixed update: ", temp)
        new_sum += temp[int(len(temp) / 2)]
    return new_sum


print("Part2: ", part2())