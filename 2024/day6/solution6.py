import sys, os
import numpy as np
from collections import defaultdict
sys.path.append('../../')
import aoc_utils



def rotate_90(ch):
    if ch == '^':
        return '>'
    elif ch == '>':
        return 'v'
    elif ch == 'v':
        return '<'
    elif ch == '<':
        return '^'
    else:
        raise Exception("not valid input")

def get_movement(ch):
    if ch == '^':
        return (-1, 0)
    elif ch == '>':
        return (0, 1)
    elif ch == 'v':
        return (1, 0)
    elif ch == '<':
        return (0, -1)
    else:
        print(ch)
        raise Exception("not valid input")


"""
ASSUMING THAT THE MAZE CAN BE ESCAPED HERE
pos is a tuple (row, col)
maze is 2D array of strings that gets changed
tried recursive, didn't work
"""
def navigate_maze(pos, maze):
    if pos[0] < 0 or pos[0] >= len(maze) or pos[1] < 0 or pos[1] >= len(maze[0]):
        return (-1, -1)
    else:
        temp_pos = get_movement(maze[pos[0]][pos[1]])
        new_pos = (temp_pos[0] + pos[0], temp_pos[1] + pos[1])
        if new_pos[0] < 0 or new_pos[0] >= len(maze) or new_pos[1] < 0 or new_pos[1] >= len(maze[0]):
            maze[pos[0]][pos[1]] = 'X'
            return (-1, -1)
        else:
            # colllide with obstacle
            if maze[new_pos[0]][new_pos[1]] == '#':
                maze[pos[0]][pos[1]] = rotate_90(maze[pos[0]][pos[1]])
                return pos
                #navigate_maze(pos, maze)
            else:
               maze[new_pos[0]][new_pos[1]] =  maze[pos[0]][pos[1]]
               maze[pos[0]][pos[1]] = "X"
               return new_pos
               #navigate_maze(new_pos, maze)
    
    
def print_maze(maze):
    for row in maze:
        print(row)

def part1():
    guard_map = list(map(lambda x: list(x), aoc_utils.return_array_from_file('./input.txt')[0]))
    start_pos = (0, 0)
    for row in range(len(guard_map)):
        for col in range(len(guard_map[0])):
            if guard_map[row][col] == '^':
                start_pos = (row, col)
    temp = start_pos
    n_m = navigate_maze(temp, guard_map)
    while n_m[0] != -1:
        n_m = navigate_maze(n_m, guard_map)


    count_X = 0
    for row in range(len(guard_map)):
        for col in range(len(guard_map[0])):
            if guard_map[row][col] == 'X':
                count_X += 1
    print_maze(guard_map)
    return count_X

def part2():
    guard_map = list(map(lambda x: list(x), aoc_utils.return_array_from_file('./input.txt')[0]))
    start_pos = (0, 0)
    for row in range(len(guard_map)):
        for col in range(len(guard_map[0])):
            if guard_map[row][col] == '^':
                start_pos = (row, col)
    num_loop_pos = 0
    for row in range(len(guard_map)):
        for col in range(len(guard_map[0])):
            if (row, col) != start_pos and guard_map[row][col] != "#":
                guard_map = list(map(lambda x: list(x), aoc_utils.return_array_from_file('./input.txt')[0]))
                guard_map[row][col] = "#"
                loop_detector = set()
                loop_detector.add((start_pos, guard_map[start_pos[0]][start_pos[1]]))
                n_m = navigate_maze(start_pos, guard_map)
                while n_m[0] != -1 and (n_m, guard_map[n_m[0]][n_m[1]]) not in loop_detector:
                    loop_detector.add((n_m, guard_map[n_m[0]][n_m[1]]))
                    n_m = navigate_maze(n_m, guard_map)
                num_loop_pos += 1 if n_m != (-1, -1) else 0
    return num_loop_pos


print("Part 2: ", part2())