import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set

    

def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0];
    num_rows = len(data)
    num_cols = len(data)
    trail_heads = []
    for row in range(len(data)):
        for col in range(len(data[0])):
            if data[row][col] == '0':
                trail_heads.append((row, col))
    
    def traverse_trail(curr_pos, curr_path, curr_nines, score):
        up = (curr_pos[0] - 1, curr_pos[1])
        down = (curr_pos[0] + 1, curr_pos[1])
        right = (curr_pos[0], curr_pos[1] + 1)
        left = (curr_pos[0], curr_pos[1] - 1)
        poss_steps = [up, down, right, left]
        for step in poss_steps:
            if step[0] < 0 or step[0] >= num_rows or step[1] < 0 or step[1] >= num_cols:
                score[0] += 0
            else:
                if int(data[step[0]][step[1]]) == int(data[curr_pos[0]][curr_pos[1]]) + 1:
                    if step in curr_path:
                        score[0] += 0
                    elif data[step[0]][step[1]] == '9' and step not in curr_nines:
                        curr_nines.add(step)
                        score[0] += 1
                    elif data[step[0]][step[1]] == '9':
                        score[0] += 0
                    else:
                        curr_path.add(curr_pos)
                        traverse_trail(step, set(curr_path), curr_nines, score)



    res = 0
    for trail_head in trail_heads:
        curr_nines = set()
        score = [0]
        traverse_trail(trail_head, set(), curr_nines, score)
        res += score[0]
    return res

print(part1())