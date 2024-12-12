import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict

def get_perimeter(region):
    region_set = set(region)
    perimeter = 0
    for element in region_set:
        above = (element[0] - 1, element[1])
        below = (element[0] + 1, element[1])
        right = (element[0], element[1] + 1)
        left = (element[0], element[1] - 1)
        perimeter += (not (above in region_set)) +(not (below in region_set )) + (not (left in region_set )) + (not (right in region_set ))
    return perimeter
def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0]
    num_rows = len(data)
    num_cols = len(data)
    def flood(flood_char, visited: Set[Tuple], curr_pos: Tuple, region: List[Tuple]):
        if curr_pos[0] >= num_rows or curr_pos[1] >= num_cols or curr_pos[0] < 0 or curr_pos[1] < 0:
            return
        else:
            if data[curr_pos[0]][curr_pos[1]] == flood_char and curr_pos not in visited:
                visited.add(curr_pos)
                region.append(curr_pos)
                flood(flood_char, visited, (curr_pos[0] + 1, curr_pos[1]), region)
                flood(flood_char, visited, (curr_pos[0] - 1, curr_pos[1]), region)
                flood(flood_char, visited, (curr_pos[0], curr_pos[1] + 1), region)
                flood(flood_char, visited, (curr_pos[0], curr_pos[1] - 1), region)
            else:
                return

    regions = []
    visited = set()
    
    for row in range(len(data)):
        for col in range(len(data[0])):
            region = []
            if (row, col) not in visited:
                flood(data[row][col], visited, (row, col), region)
                regions.append(region)
    res = 0
    for r in regions:
        res += len(r) * get_perimeter(r)

    return res



print("Part 1: ", part1())
