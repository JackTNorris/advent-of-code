import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def part1():
    global directions
    data = aoc_utils.return_array_from_file('./input.txt')[0]
    my_map = [['.' for _ in range(71)] for _ in range(71)]

    for i in range(1024):
        coord_x, coord_y = data[i].split(',')
        my_map[int(coord_y)][int(coord_x)] = '#'
    
    djikstra_map = [[float('inf') for _ in range(71)] for _ in range(71)]
    djikstra_map[0][0] = 0
    to_visit = [(0, (0, 0))]
    heapq.heapify(to_visit)
    while len(to_visit) > 0:
        curr_dist, curr_pos = heapq.heappop(to_visit)
        if my_map[curr_pos[0]][curr_pos[1]] == '#':
            continue
        if curr_dist > djikstra_map[curr_pos[0]][curr_pos[1]]:
            continue
        for d in directions:
            temp = (curr_pos[0] + d[0], curr_pos[1] + d[1])
            if temp[0] < 0 or temp[0] > 70:
                continue
            if temp[1] < 0 or temp[1] > 70:
                continue
            if djikstra_map[temp[0]][temp[1]] > curr_dist + 1:
                djikstra_map[temp[0]][temp[1]] = curr_dist + 1
                heapq.heappush(to_visit, (curr_dist + 1, temp))
    print(djikstra_map[70][70])
        
    return None

print("Part 1: ", part1())