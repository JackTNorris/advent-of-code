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

def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0]
    num_cols = 101 # wide
    num_rows = 103 # tall
    iterations = 100
    robots = []

    for line in data:
        position_string, velocity_string = line.split(' ')
        position = list(map(lambda x: int(x), position_string.split('=')[1].split(',')))
        velocity = list(map(lambda x: int(x), velocity_string.split('=')[1].split(',')))
        robots.append({'p': position, 'v': velocity})

    # get end position for each robot

    for robot in robots:
        pos = robot['p']
        vel = robot['v']
        for i in range(iterations):
            pos[0] += vel[0]
            pos[1] += vel[1]
            if pos[0] >= num_cols:
                pos[0] -= (num_cols)
            if pos[1] >= num_rows:
                pos[1] -= (num_rows)
            if pos[0] < 0:
                pos[0] += num_cols
            if pos[1] < 0:
                pos[1] += num_rows
    
    def get_quadrant(pos):
        if pos[0] == int(num_cols / 2) or pos[1] == int(num_rows / 2):
            return -1
        elif pos[0] > int(num_cols / 2):
            if pos[1] > int(num_rows / 2):
                return 4
            if pos[1] < int(num_rows / 2):
                return 1
        elif pos[0] < int(num_cols / 2):
            if pos[1] > int(num_rows / 2):
                return 3
            if pos[1] < int(num_rows / 2):
                return 2
    
    robo_quadrants = defaultdict(lambda: 0)
    for robot in robots:
        q = get_quadrant(robot['p'])
        if q != -1:
            robo_quadrants[q] += 1
    
    res = 1
    for i in range(1, 5):
        res *= robo_quadrants[i]
    return res



def part2():
    data = aoc_utils.return_array_from_file('./input.txt')[0]
    num_cols = 101 # wide
    num_rows = 103 # tall
    iterations = 0
    robots = []

    for line in data:
        position_string, velocity_string = line.split(' ')
        position = list(map(lambda x: int(x), position_string.split('=')[1].split(',')))
        velocity = list(map(lambda x: int(x), velocity_string.split('=')[1].split(',')))
        robots.append({'p': position, 'v': velocity})

    robot_tuple_set = set()
    robot_tuple_list = []
    robot_tuple = (0, 0)

    
    # find cycle to know range to go to
    while robot_tuple not in robot_tuple_set:
        # get end position for each robot
        iterations += 1
        if robot_tuple != (0,0):
            robot_tuple_set.add(robot_tuple)
            robot_tuple_list.append(robot_tuple)
        for robot in robots:
            pos = robot['p']
            vel = robot['v']
            pos[0] += vel[0]
            pos[1] += vel[1]
            if pos[0] >= num_cols:
                pos[0] -= (num_cols)
            if pos[1] >= num_rows:
                pos[1] -= (num_rows)
            if pos[0] < 0:
                pos[0] += num_cols
            if pos[1] < 0:
                pos[1] += num_rows
        robot_tuple = tuple(map(lambda x: tuple(x['p']), robots))
    
    iteration = 0
    for robot_tuple in robot_tuple_list:
        iteration += 1
        # this is subject to change for every person
        if iteration > 7000:
            img = Image.new( 'RGB', (101,103), "white") # Create a new black image
            pixels = img.load() # Create the pixel map
            for i in range(img.size[0]):    # For every pixel:
                for j in range(img.size[1]):
                    if (i, j) in robot_tuple:
                        pixels[i,j] = (0, 0, 0) # Set the colour accordingly
            img.save('./img/' + str(iteration) + '.bmp')
    return iterations

part2()
print('got 7051 for this by rendering bitmaps, looking, and submitting shite answers to narrow down the range')
