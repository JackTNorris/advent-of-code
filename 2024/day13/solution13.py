import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict

def lcm(n1: int, n2: int):
    s1 = n1
    s2 = n2
    while s1 != s2:
        if s1 < s2:
            s1 += n1
        elif s1 > s2:
            s2 += n2
    return s1

def part1():
    data = aoc_utils.return_array_from_file('./input.txt')
    res = 0
    for scenario in data:
        button_a_instructions = scenario[0].split(': ')[1]
        button_b_instructions = scenario[1].split(': ')[1]
        prize_instructions = scenario[2].split(': ')[1]
        
        button_a_int_moves = list(map(lambda x: int(x[2:])  , button_a_instructions.split(', ')))
        button_b_int_moves = list(map(lambda x: int(x[2:])  , button_b_instructions.split(', ')))
        prize_int = list(map(lambda x: int(x[2:])  , prize_instructions.split(', ')))
        
        a_lcm = lcm(button_a_int_moves[0], button_a_int_moves[1])

        temp_button_a_int_moves = [button_a_int_moves[0] * (a_lcm / button_a_int_moves[0]), button_a_int_moves[1] * (a_lcm / button_a_int_moves[1])]
        temp_button_b_int_moves = [button_b_int_moves[0] * (a_lcm / button_a_int_moves[0]), button_b_int_moves[1] * (a_lcm / button_a_int_moves[1])]
        temp_prize_int = [prize_int[0] * (a_lcm / button_a_int_moves[0]), prize_int[1] * (a_lcm / button_a_int_moves[1])]

        l_side = temp_prize_int[0] - temp_prize_int[1]
        r_side = temp_button_b_int_moves[0] - temp_button_b_int_moves[1]
        
        b_sol = l_side / r_side

        if not b_sol.is_integer():
            continue
        a_sol = (prize_int[0] - b_sol * button_b_int_moves[0]) / button_a_int_moves[0]
        if not a_sol.is_integer():
            continue
        
        if a_sol > 100 or b_sol > 100:
            continue
        res += b_sol + a_sol * 3
    return res

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')
    res = 0
    for scenario in data:
        button_a_instructions = scenario[0].split(': ')[1]
        button_b_instructions = scenario[1].split(': ')[1]
        prize_instructions = scenario[2].split(': ')[1]
        
        button_a_int_moves = list(map(lambda x: int(x[2:])  , button_a_instructions.split(', ')))
        button_b_int_moves = list(map(lambda x: int(x[2:])  , button_b_instructions.split(', ')))
        prize_int = list(map(lambda x: int(x[2:]) + 10000000000000  , prize_instructions.split(', ')))
        
        a_lcm = lcm(button_a_int_moves[0], button_a_int_moves[1])

        temp_button_a_int_moves = [button_a_int_moves[0] * (a_lcm / button_a_int_moves[0]), button_a_int_moves[1] * (a_lcm / button_a_int_moves[1])]
        temp_button_b_int_moves = [button_b_int_moves[0] * (a_lcm / button_a_int_moves[0]), button_b_int_moves[1] * (a_lcm / button_a_int_moves[1])]
        temp_prize_int = [prize_int[0] * (a_lcm / button_a_int_moves[0]), prize_int[1] * (a_lcm / button_a_int_moves[1])]

        l_side = temp_prize_int[0] - temp_prize_int[1]
        r_side = temp_button_b_int_moves[0] - temp_button_b_int_moves[1]
        
        b_sol = l_side / r_side

        if not b_sol.is_integer():
            continue
        a_sol = (prize_int[0] - b_sol * button_b_int_moves[0]) / button_a_int_moves[0]
        if not a_sol.is_integer():
            continue
        
        res += b_sol + a_sol * 3
    return res

print("Part 2: ", part2())