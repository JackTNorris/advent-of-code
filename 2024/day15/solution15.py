import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
from PIL import Image


def get_end_pos(robot, moves, num_cols, num_rows, iters):
    first_spot = robot['p']
    velocity = robot['v']

def gps_sum(ware_house_map):
    res = 0
    for row in range(len(ware_house_map)):
        for col in range(len(ware_house_map[0])):
            if ware_house_map[row][col] == 'O':
                res += row * 100 + col
    return res

def get_change_from_move_char(move_char):
    if move_char == '<':
        return [0, -1]
    if move_char == '>':
        return [0, 1]
    if move_char == '^':
        return [-1, 0]
    if move_char == 'v':
        return [1, 0]
    return [-1, -1]

def perform_move(robot_pos: List[int], initial_warehouse_state, move_char):
    temp_ware_house = list(map(lambda x: list(x), initial_warehouse_state[:]))
    new_robot_pos = robot_pos[:]
    move_arr = get_change_from_move_char(move_char)
    def has_spare_space(pos, move_char):
        if initial_warehouse_state[pos[0]][pos[1]] == '.':
            return True
        elif initial_warehouse_state[pos[0]][pos[1]] == '#':
            return False
        else:
            return has_spare_space([pos[0] + move_arr[0], pos[1] + move_arr[1]], move_char)
    
    if has_spare_space(robot_pos[:], move_char):
        new_robot_pos = [new_robot_pos[0] + move_arr[0], new_robot_pos[1] + move_arr[1]]
        temp_ware_house[robot_pos[0]][robot_pos[1]] = '.'
        temp_pos = robot_pos[:]
        booted = '@'
        index = 0
        while booted != '.':
            temp_pos = [temp_pos[0] + move_arr[0], temp_pos[1] + move_arr[1]]
            temp_booted = booted
            booted = temp_ware_house[temp_pos[0]][temp_pos[1]]
            temp_ware_house[temp_pos[0]][temp_pos[1]] = temp_booted

    return (new_robot_pos, list(map(lambda x: "".join(x), temp_ware_house)))


def part1():
    data = aoc_utils.return_array_from_file('./input.txt')
    ware_house_map = data[0]
    move_string = "".join(data[1])
    robot_pos = []
    # get_initial_robot_coordinates
    for row in range(len(ware_house_map)):
        for col in range(len(ware_house_map[0])):
            if ware_house_map[row][col] == '@':
                robot_pos = [row, col]


    for move in move_string:
        robot_pos, ware_house_map = perform_move(robot_pos, ware_house_map, move)
    return gps_sum(ware_house_map)

print("Part 1: ", part1())

