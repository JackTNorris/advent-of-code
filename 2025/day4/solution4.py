#!/usr/bin/env python3

import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict

# hacky as crap, but oiko
def part1(data: List[str]):
    res = 0
    def adj_coords(pos):
        return [
                (pos[0]+1, pos[1]),
                (pos[0]+1, pos[1]+1),
                (pos[0]+1, pos[1]-1),
                (pos[0]-1, pos[1]),
                (pos[0]-1, pos[1]+1),
                (pos[0]-1, pos[1]-1),
                (pos[0], pos[1]+1),
                (pos[0], pos[1]-1),
            ]

    def calc_adj_rolls(pos):
        num_adj = 0
        adjs = adj_coords(pos)
        for coord in adjs:
            if coord[0] >= 0 and coord[0] < len(data):
                if coord[1] >= 0 and coord[1] < len(data[coord[0]]):
                    if data[coord[0]][coord[1]] == '@':
                        num_adj += 1
                        if num_adj == 4:
                            return num_adj
        return num_adj

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '@' and calc_adj_rolls((i, j)) <= 3:
                res += 1
    return res 
    
    

# looking to make the biggest 12 digit number from the input
def part2(data: List[str]):
    res = 0
    def adj_coords(pos):
        return [
                (pos[0]+1, pos[1]),
                (pos[0]+1, pos[1]+1),
                (pos[0]+1, pos[1]-1),
                (pos[0]-1, pos[1]),
                (pos[0]-1, pos[1]+1),
                (pos[0]-1, pos[1]-1),
                (pos[0], pos[1]+1),
                (pos[0], pos[1]-1),
            ]

    def calc_adj_rolls(pos):
        num_adj = 0
        adjs = adj_coords(pos)
        for coord in adjs:
            if coord[0] >= 0 and coord[0] < len(data):
                if coord[1] >= 0 and coord[1] < len(data[coord[0]]):
                    if data[coord[0]][coord[1]] == '@':
                        num_adj += 1
                        if num_adj == 4:
                            return num_adj
        return num_adj
    data = list(map(lambda x: list(x), data))
    temp_res = -1
    while res != temp_res:
        temp_res = res
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == '@' and calc_adj_rolls((i, j)) <= 3:
                    data[i][j] = '.'
                    res += 1
    return res 
    
if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1: ", part1(data[0]))
    print("Part 2: ", part2(data[0]))