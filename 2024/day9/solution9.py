import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple


def compute_checksum(input):
    check_sum = 0
    for i in range(len(input)):
        if input[i] == -1:
            break
        check_sum += i * int(input[i])
    return check_sum

def generate_blocks(input):
    res = []
    indexer = 0
    for i in range(0, len(input), 2):
        if i == len(input) - 1:
            res += [indexer] * (max(int(input[i]), 1))
            break
        else:
            res += [indexer] * int(input[i]) + [-1] * int(input[i + 1])
        indexer += 1
    return res

def fragment(data):
    bottom, top = 0, len(data) - 1
    while bottom < top:
        while data[top] == -1:
            top-=1
        while data[bottom] != -1:
            bottom += 1
        if top < bottom:
            break
        else:
            data[top], data[bottom] = data[bottom], data[top]
    return data

def generate_blocks2(input):
    # marking file beginning and ends with [-2]
    res = []
    indexer = 0
    for i in range(0, len(input), 2):
        res += [-2]
        if i == len(input) - 1:
            res += [indexer] * (max(int(input[i]), 1))
            res += [-2]
            break
        else:
            res += [indexer] * int(input[i]) + [-2] + [-1] * int(input[i + 1])
        indexer += 1
    return res

def fragment2(data: List[int]):
    def get_gap(index):
        gap_start = index
        while index < len(data) and data[index] == -1:
            index += 1
        return (gap_start, index)
    def get_file(index):
        end_index = index
        index = index - 1
        while index >= 0 and data[index] != -2:
            index -= 1
        return (index + 1, end_index)

    file_set = set()
    # blocks marked with -2
    bottom, top = 0, len(data) - 1
    while top > bottom:
        while data[top] == -1:
            top-=1
        while data[bottom] != -1:
            bottom += 1
        if bottom > top:
            break
        gap_indices = (get_gap(bottom))
        file_indices = (get_file(top))
        if tuple(data[file_indices[0]: file_indices[1]]) in file_set:
            top = file_indices[0] - 2
            continue
        else:
            file_set.add(tuple(data[file_indices[0]: file_indices[1]]))
        while not (gap_indices[1] - gap_indices[0] >= file_indices[1] - file_indices[0]):
            temp = gap_indices[1] + 1
            while temp < len(data) and data[temp] != -1:
                temp += 1
            if temp >= len(data):
                break
            gap_indices = get_gap(temp)  
            if gap_indices[0] > file_indices[0] or gap_indices[0] == gap_indices[1]:
                break
        # perform a swap
        if gap_indices[1] - gap_indices[0] >= file_indices[1] - file_indices[0]  and gap_indices[0] < file_indices[0]:
            file_length = file_indices[1] - file_indices[0]
            temp_file = data[file_indices[0] - 1: file_indices[1] + 1]
            data[file_indices[0] - 1: file_indices[1] + 1] = [-3] + [-1] * (file_indices[1] - (file_indices[0]))
            data[gap_indices[0]: gap_indices[0] + file_length] = temp_file
            top = data.index(-3)
            data[top:top+1] = []
        else:
            top = file_indices[0] - 2
    return data


def compute_checksum2(input):
    check_sum = 0
    for i in range(len(input)):
        if input[i] == -1:
            check_sum += 0
        else:
            check_sum += i * int(input[i])
    return check_sum

def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0][0];
    data = generate_blocks(data)
    data = fragment(data)
    data = compute_checksum(data)
    return data

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')[0][0];
    data = generate_blocks2(data)
    print("Generated blocks")
    data = fragment2(data)
    print("Fragmented")
    #print("".join(map(lambda x: str(x), filter(lambda x: x != -2, map(lambda x: '.' if x == -1 else x, data)))))
    print("Doing checksum")
    data = compute_checksum2(list(filter(lambda x: x != -2, data)))
    return data

print(part2())