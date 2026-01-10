#!/usr/bin/env python3
from typing import List
import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict
import math


def calc_rect_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def part1(data):
    res = 0
    for i in range(len(data)):
        [x1, y1] = map(int, data[i].split(','))
        for j in range(i + 1, len(data)):
            [x2, y2] = map(int, data[j].split(','))
            res = max(res, calc_rect_area((x1, y1), (x2, y2)))
    return res

    

def part2(data: List[str]):
    return 0
    

if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1: ", part1(data[0]))
    #print("Part 2: ", part2(data[0]))
