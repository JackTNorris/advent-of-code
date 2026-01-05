#!/usr/bin/env python3
from typing import List
import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict

def op_calculator(op, items):
    items = list(filter(lambda x: x != '', items))
    r = int(items[0])
    for i in range(1, len(items)):
        if op == '+':
            r += int(items[i])
        if op == '*':
            r *= int(items[i])
    return r

def part1(data):
    res = 0
    ops = data[-1].split()
    items = list(map(lambda x: x.split(), data[:-1]))
    items = [*zip(*items)]
    for i in range(len(ops)):
        res += op_calculator(ops[i], items[i])
    return res

    

def part2(data: List[str]):
    res = 0
    ops = data[-1].split()
    items = data[:-1]
    items = [*zip(*items)]
    new_items = []
    temp = []
    for i in items:
        g = "".join(i)
        if g.isspace():
            new_items.append(list(filter(lambda x: x != '', temp)))
            temp = []
        else:
            temp.append(g.strip())
    if len(temp) > 0:
        new_items.append(list(filter(lambda x: x != '', temp)))
    for i in range(len(ops)):
        res += op_calculator(ops[i], new_items[i])
    return res

if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1: ", part1(data[0]))
    print("Part 2: ", part2(data[0]))