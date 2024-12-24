import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy


n, s, e, w = (-1, 0), (1, 0), (0,- 1), (0, 1)
directions = [n, s, e, w]

def dir_to_keypad(dir):
    if dir == (-1, 0):
        return '^'
    elif dir == (0, -1):
        return '<'
    elif dir == (1, 0):
        return 'v'
    elif dir == (0, 1):
        return '>'
    else:
        raise Exception("Invalid robot keypad action")

def numeric_coord_from_key(key):
    if key == '7':
        return (0, 0)
    if key == '8':
        return (0, 1)
    if key == '9':
        return (0, 2)
    if key == '4':
        return (1, 0)
    if key == '5':
        return (1, 1)
    if key == '6':
        return (1, 2)
    if key == '1':
        return (2, 0)
    if key == '2':
        return (2, 1)
    if key == '3':
        return (2, 2)  
    if key == None:
        return (3, 0)
    if key == '0':
        return (3, 1)
    if key == 'A':
        return (3, 2) 
def numeric_key_from_coord(coord):
    if coord == (0, 0):
        return '7'
    if coord == (0, 1):
        return '8'
    if coord == (0, 2):
        return '9'
    if coord == (1, 0):
        return '4'
    if coord == (1, 1):
        return '5'
    if coord == (1, 2):
        return '6'
    if coord == (2, 0):
        return '1'
    if coord == (2, 1):
        return '2'
    if coord == (2, 2):
        return '3'
    if coord == (3, 0):
        return None
    if coord == (3, 1):
        return '0'
    if coord == (3, 2):
        return 'A'


def direction_coord_from_Key(key):
    if key == '^':
        return (0, 1)
    elif key == 'A':
        return (0, 2)
    elif key == '<':
        return (1, 0)
    elif key == 'v':
        return (1, 1)
    elif key == '>':
        return (1, 2)
    elif key == None:
        return (0, 0)
    else:
        raise Exception("Invalid robot keypad")



def key_from_direction_coord(coord):
    if coord == (0, 1):
        return '^'
    elif coord == (0, 2):
        return 'A'
    elif coord == (1, 0):
        return '<'
    elif coord == (1, 1):
        return 'v'
    elif coord == (1, 2):
        return '>'
    elif coord == (0, 0):
        return None
    else:
        raise Exception("Invalid direction coordinate")


def recursive_bfs_all_paths(grid, queue, dest, path, all_paths, dir_path, dir_all_paths):
    if not queue:  # Base case: queue is empty
        return (all_paths, dir_all_paths)
    # Dequeue the first element
    (current_path, curr_dir_path) = queue.pop(0)
    coords = current_path[-1]

    if coords[0] < 0 or coords[0] >= len(grid) or coords[1] < 0 or coords[1] >= len(grid[0]):
        return (all_paths, dir_all_paths)
    # Check if we've reached the destination
    if coords == dest:
        all_paths.append(current_path)
        dir_all_paths.append(curr_dir_path)

    else:
        for d in directions:
            temp = (coords[0] + d[0], coords[1] + d[1])
            if temp[0] >= 0 and temp[0] < len(grid) and temp[1] >= 0 and temp[1] < len(grid[0]):
                if temp not in current_path:
                    if grid[temp[0]][temp[1]] != None:
                        queue.append((current_path + [temp], curr_dir_path + [dir_to_keypad(d)]))

    # Recursive call with updated queue and paths
    return recursive_bfs_all_paths(grid, queue, dest, path, all_paths, dir_path, dir_all_paths)

def find_all_routes(grid, src, dest):
    queue = [([src], [])]  # Initialize the queue with the start node as a path
    all_paths = []
    dir_all_paths = []
    return sorted(recursive_bfs_all_paths(grid, queue, dest, [], all_paths, [], dir_all_paths), key=lambda x: len(x))

def part1():
    data = aoc_utils.return_array_from_file('input.txt')[0]
    def calc_complexity(c, seq):
        return len(seq) * int(c[:-1])

    numeric_keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
    directional_keypad = [[None, '^', 'A'], ['<', 'v', '>']]
    num_robots = 2

    numeric_bfs_sols = {}
    dir_bfs_sols = {}
    res = 0

    # numeric_possibilities
    for code in data:
        possibilities = []
        prev = ""
        # for every character in the code
        for i in range(len(code)):
            if i == 0:
                if ((3, 2), numeric_coord_from_key(code[i])) in numeric_bfs_sols:
                    pos_directions = numeric_bfs_sols[((3, 2), numeric_coord_from_key(code[i]))]
                else:
                    _, pos_directions = find_all_routes(numeric_keypad, (3, 2), numeric_coord_from_key(code[i]))
                    numeric_bfs_sols[((3, 2), numeric_coord_from_key(code[i]))] = deepcopy(pos_directions)
                min_poss_length =len(min(pos_directions, key=len))
                pos_directions = list(filter(lambda x: len(x) == min_poss_length, pos_directions))
                for d in pos_directions:
                    possibilities.append("".join(d) + 'A')
            else:
                if (numeric_coord_from_key(prev), numeric_coord_from_key(code[i])) in numeric_bfs_sols:
                    pos_directions = numeric_bfs_sols[(numeric_coord_from_key(prev), numeric_coord_from_key(code[i]))]
                else:
                    _, pos_directions = find_all_routes(numeric_keypad, numeric_coord_from_key(prev), numeric_coord_from_key(code[i]))
                    numeric_bfs_sols[(numeric_coord_from_key(prev), numeric_coord_from_key(code[i]))] = deepcopy(pos_directions)
                temp_len = len(possibilities)
                min_poss_length =len(min(pos_directions, key=len))
                pos_directions = list(filter(lambda x: len(x) == min_poss_length, pos_directions))
                temp_shit = []
                for d in pos_directions:
                    temp = []
                    for g in range(temp_len):
                        temp.append(possibilities[g] + "".join(d) + 'A')
                    temp_shit += temp
                possibilities = temp_shit
            prev = code[i]
        min_poss_length =len(min(possibilities, key=len))
        possibilities = list(filter(lambda x: len(x) == min_poss_length, possibilities))
        for i in range(num_robots):
            #now directional keypads
            end_pos = []
            for poss in possibilities:
                directional_possibilities = []
                prev = ""
                for c in range(len(poss)):
                    if c == 0:
                        if ((0, 2), direction_coord_from_Key(poss[c])) in dir_bfs_sols:
                            pos_directions = dir_bfs_sols[((0, 2), direction_coord_from_Key(poss[c]))]
                        else:
                            _, pos_directions = find_all_routes(directional_keypad, (0, 2), direction_coord_from_Key(poss[c]))
                            dir_bfs_sols[((0, 2), direction_coord_from_Key(poss[c]))] = deepcopy(pos_directions)
                        min_poss_length =len(min(pos_directions, key=len))
                        pos_directions = list(filter(lambda x: len(x) == min_poss_length, pos_directions))
                        for d in pos_directions:
                            directional_possibilities.append("".join(d) + 'A')
                    else:
                        if (direction_coord_from_Key(prev), direction_coord_from_Key(poss[c])) in dir_bfs_sols:
                            pos_directions = dir_bfs_sols[(direction_coord_from_Key(prev), direction_coord_from_Key(poss[c]))]
                        else:
                            _, pos_directions = find_all_routes(directional_keypad, direction_coord_from_Key(prev), direction_coord_from_Key(poss[c]))
                            dir_bfs_sols[(direction_coord_from_Key(prev), direction_coord_from_Key(poss[c]))] = deepcopy(pos_directions)
                        min_poss_length =len(min(pos_directions, key=len))
                        pos_directions = list(filter(lambda x: len(x) == min_poss_length, pos_directions))
                        temp_len = len(directional_possibilities)
                        temp_shit = []
                        for d in pos_directions:
                            temp = []
                            for g in range(temp_len):
                                temp.append(directional_possibilities[g] + "".join(d) + 'A')
                            temp_shit += temp
                        directional_possibilities = temp_shit
                    prev = poss[c]
                min_poss_length =len(min(directional_possibilities, key=len))
                directional_possibilities = list(filter(lambda x: len(x) == min_poss_length, directional_possibilities))
                end_pos += directional_possibilities
            min_poss_length =len(min(end_pos, key=len))
            end_pos = list(filter(lambda x: len(x) == min_poss_length, end_pos))
            possibilities = end_pos
        print("LENGTH FOR: ", code)
        res += calc_complexity(code, possibilities[0])
        print(len(possibilities[0]))

    return res
print("Part 1: ", part1())
    