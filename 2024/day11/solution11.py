import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict

    

def blink(arr):
    new_arr = []
    for element in arr:
        if element == 0:
            new_arr.append(1)
        elif len(str(element)) % 2 == 0:
            temp = str(element)
            front_half = int(temp[:int(len(temp)/2)])
            second_half = int(temp[int(len(temp)/2):])
            new_arr.append(front_half)
            new_arr.append(second_half)
        else:
            new_arr.append(element * 2024)
    return new_arr
        

def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0][0];
    stones = list(map(lambda x: int(x), data.split(' ')))
    num_blinks = 75
    for i in range(num_blinks):
        stones = blink(stones)
    return len(stones)

def blink2(dict: Dict[int, int]):
    new_dict = defaultdict(lambda: 0)
    for item in dict.keys():
        count = dict[item]
        if item == 0:
            new_dict[1] += count
        elif len(str(item)) % 2 == 0:
            temp = str(item)
            front_half = int(temp[:int(len(temp)/2)])
            second_half = int(temp[int(len(temp)/2):])
            new_dict[front_half] += count
            new_dict[second_half] += count
        else:
            new_dict[item * 2024] += count
    return new_dict

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')[0][0];
    temp_stones = list(map(lambda x: int(x), data.split(' ')))
    stones = defaultdict(lambda: 0)
    for s in temp_stones:
        stones[s] += 1
    num_blinks = 75
    for i in range(num_blinks):
        stones = blink2(stones)
    total_count = 0
    for stone in stones.keys():
        total_count += stones[stone]
    return total_count


print("Part 1: ", part1())
print("Part 2: ", part2())