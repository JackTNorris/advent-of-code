#!/usr/bin/env python3

import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict

def part1(ranges, ids):
    res = 0
    for id in ids:
        int_id = int(id)
        for r in ranges:
            r1, r2 = list(map(int, r.split('-')))
            r2 -= int_id
            temp_int_id = int_id - r1
            if temp_int_id >= 0 and r2 >= 0:
                res += 1
                break
    return res
    

# looking to make the biggest 12 digit number from the input
def part2(ranges, ids):
    # too low: 333404221810494
    #.         360341832208407
    res = 0
    sorted_ranges = list(map(lambda x: tuple(x.split('-')), sorted(ranges, key=lambda x: int(x.split('-')[0]))))
    print(sorted_ranges)
    prev = (-1, -1)
    for r in sorted_ranges:
        if prev == (-1, -1):
            res += max(0, int(r[1]) - int(r[0]) + 1)
            prev = (int(r[0]), int(r[1]))
        else:
            if prev[1] < int(r[0]):
                res += max(0, int(r[1]) - int(r[0]) + 1)
                prev = (min(prev[0],  int(r[0])), max(int(r[1]), prev[1]))
            else:
                res += max(0, int(r[1]) - prev[1])
                prev = (min(prev[0],  int(r[0])), max(int(r[1]), prev[1]))
    return res

if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')

    print("Part 1: ", part1(data[0], data[1]))
    print("Part 2: ", part2(data[0], data[1]))