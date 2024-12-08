import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple


def get_possible_antinodes(a1: Tuple[int], a2: Tuple[int]):
    diff_vec = (a2[0] - a1[0], a2[1] - a1[1])
    n1 = (a2[0] + diff_vec[0], a2[1] + diff_vec[1])
    n2 = (a1[0] - diff_vec[0], a1[1] - diff_vec[1])
    return [n1, n2]

def get_possible_antinodes_p2(a1: Tuple[int], a2: Tuple[int], num_rows: int, num_cols: int):
    # get diff vector (a1 to a2)
    diff_vec = [a2[0] - a1[0], a2[1] - a1[1]]
    # calculate grid "unit vector":
    gcd = math.gcd(diff_vec[0], diff_vec[1])
    diff_vec[0], diff_vec[1] = diff_vec[0] / gcd, diff_vec[1] / gcd
    temp = diff_vec[::]
    pos = a1[::]
    res = [pos[::]]
    while pos[0] >= 0 and pos[0] < num_rows and pos[1] >= 0 and pos[1] < num_cols:
        pos = (pos[0] + diff_vec[0], pos[1] + diff_vec[1])
        res.append(pos[::])
    pos = a1[::]
    while pos[0] >= 0 and pos[0] < num_rows and pos[1] >= 0 and pos[1] < num_cols:
        pos = (pos[0] - diff_vec[0], pos[1] - diff_vec[1])
        res.append(pos[::])
    return res
    
    
    

def generate_antenna_loc_pairs(antenna_locs):
    pairs = []
    for i in range(len(antenna_locs)):
        for j in range(i + 1, len(antenna_locs)):
            pairs.append((antenna_locs[i], antenna_locs[j]))
    return pairs


def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0];
    antennas = defaultdict(lambda: [])
    num_rows = len(data)
    num_cols = len(data[0])
    # edge case: antinodes at the same spot?
    anti_nodes_set = set()
    # get the antenna location
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] != '.':
                antennas[data[row][col]].append((row, col))

    # loop through each antenna type, calculating paris
    for antenna_class in antennas.keys():
        antenna_locs = antennas[antenna_class]
        pairs = generate_antenna_loc_pairs(antenna_locs)
        for pair in pairs:
            # calculate anti-node, verify in map, stick it in a set for unique nodes
            poss_anti_nodes = get_possible_antinodes(pair[0], pair[1])
            for n in poss_anti_nodes:
                # valid position
                if not (n[0] >= num_rows or n[1] >= num_cols or n[0] < 0 or n[1] < 0):
                    anti_nodes_set.add(n)    
    return len(anti_nodes_set)

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')[0];
    antennas = defaultdict(lambda: [])
    num_rows = len(data)
    num_cols = len(data[0])
    # edge case: antinodes at the same spot?
    anti_nodes_set = set()
    # get the antenna location
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] != '.':
                antennas[data[row][col]].append((row, col))

    # loop through each antenna type, calculating paris
    for antenna_class in antennas.keys():
        antenna_locs = antennas[antenna_class]
        pairs = generate_antenna_loc_pairs(antenna_locs)
        for pair in pairs:
            # calculate anti-node, verify in map, stick it in a set for unique nodes
            poss_anti_nodes = get_possible_antinodes_p2(pair[0], pair[1], num_rows, num_cols)
            for n in poss_anti_nodes:
                # valid position
                if not (n[0] >= num_rows or n[1] >= num_cols or n[0] < 0 or n[1] < 0):
                    anti_nodes_set.add(n)    
    return len(anti_nodes_set)

print("Part 1: ", part1())
print("Part 2: ", part2())