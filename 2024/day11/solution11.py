import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set

    

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
    num_blinks = 25
    for i in range(num_blinks):
        stones = blink(stones)
    return len(stones)

print(part1())