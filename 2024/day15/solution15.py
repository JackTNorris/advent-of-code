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


def new_gps_sum(ware_house):
    num_rows = len(ware_house)
    num_cols = len(ware_house[0])
    res = 0
    for row in range(num_rows):
        for col in range(num_cols):
            rf = 100
            cf = 1
            if ware_house[row][col] == '[':
                # instructions for this part were kinda shit, initially though I should do this
                """
                if col < int(num_cols/2):
                    cf *= col
                else:
                    cf *= (num_cols - col) - 2
                if row < int(num_rows / 2):
                    rf *= row
                else:
                    rf *= (num_rows - row) - 1
                """
                rf *= row
                cf *= col
                res += rf + cf
    return res

def new_perform_move(robot_pos: List[int], initial_warehouse_state, move_char):
    temp_ware_house = list(map(lambda x: list(x), initial_warehouse_state[:]))
    new_robot_pos = robot_pos[:]
    move_arr = get_change_from_move_char(move_char)
    def has_spare_space(pos, move_char, to_move):
        if initial_warehouse_state[pos[0]][pos[1]] == '.':
            return True
        elif initial_warehouse_state[pos[0]][pos[1]] == '#':
            return False
        else:
            to_move.append(tuple(pos))
            if initial_warehouse_state[pos[0]][pos[1]] == '[' and move_arr[0] != 0:
                to_move.append(tuple([pos[0], pos[1] + move_arr[1] + 1]))
                return has_spare_space([pos[0] + move_arr[0], pos[1] + move_arr[1]], move_char,to_move) and has_spare_space([pos[0] + move_arr[0], pos[1] + move_arr[1] + 1], move_char,to_move)
            elif initial_warehouse_state[pos[0]][pos[1]] == ']' and move_arr[0] != 0:
                to_move.append(tuple([pos[0], pos[1] + move_arr[1] - 1])) 
                return has_spare_space([pos[0] + move_arr[0], pos[1] + move_arr[1]], move_char,to_move) and has_spare_space([pos[0] + move_arr[0], pos[1] + move_arr[1] - 1], move_char,to_move)
            else:
                return has_spare_space([pos[0] + move_arr[0], pos[1] + move_arr[1]], move_char, to_move)

    # good enough up to here, need to refactor rest though
    to_move = []
    if has_spare_space(robot_pos[:], move_char, to_move):
        to_move = list(set(to_move))
        new_robot_pos = [new_robot_pos[0] + move_arr[0], new_robot_pos[1] + move_arr[1]]
        if move_arr[0] != 0:
            if move_char == '^':
                to_move = sorted(to_move, key=lambda x: x[0])
            elif move_char == 'v':
                to_move = sorted(to_move, key=lambda x: x[0], reverse=True)
            for pos in to_move:
                temp_pos = [pos[0] + move_arr[0], pos[1]]
                temp_ware_house[temp_pos[0]][temp_pos[1]] = temp_ware_house[pos[0]][pos[1]]
                temp_ware_house[pos[0]][pos[1]] = '.'
        else:
            temp_ware_house[robot_pos[0]][robot_pos[1]] = '.'
            temp_pos = robot_pos[:]
            booted = '@'
            while booted != '.':
                temp_pos = [temp_pos[0] + move_arr[0], temp_pos[1] + move_arr[1]]
                temp_booted = booted
                booted = temp_ware_house[temp_pos[0]][temp_pos[1]]
                temp_ware_house[temp_pos[0]][temp_pos[1]] = temp_booted

    return (new_robot_pos, list(map(lambda x: "".join(x), temp_ware_house)))

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')
    ware_house_map = data[0]
    ware_house_map = data[0]
    move_string = "".join(data[1])
    new_ware_house = []
    robot_pos = []
    # expand warehouse:
    
    for row in range(len(ware_house_map)):
        new_line = ""
        for col in range(len(ware_house_map[0])):
            if ware_house_map[row][col] == 'O':
                new_line += '[]'
            elif ware_house_map[row][col] == '#':
                new_line += '##'
            elif ware_house_map[row][col] == '.':
                new_line += '..'
            elif ware_house_map[row][col] == '@':
                new_line += '@.'
        new_ware_house.append(new_line)
    ware_house_map = new_ware_house
    
    # get_initial_robot_coordinates
    for row in range(len(ware_house_map)):
        for col in range(len(ware_house_map[0])):
            if ware_house_map[row][col] == '@':
                robot_pos = [row, col]
    for move in move_string:
        robot_pos, ware_house_map = new_perform_move(robot_pos, ware_house_map, move)
    return new_gps_sum(ware_house_map)

print("Part 2: ", part2())

