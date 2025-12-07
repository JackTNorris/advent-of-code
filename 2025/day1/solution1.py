#!/usr/bin/env python3
import sys
sys.path.append('../../')
import aoc_utils
import math

def part1(data):
    res = 0
    pos = 50
    for line in data:
        direction = line[0]
        num_rot = int(line[1:])
        if direction == 'L':
            pos = ((pos - num_rot) % 100)
        else:
            pos = abs(pos + num_rot) % 100
        if pos == 0:
            res += 1
    return res


def part2(data):
    res = 0
    pos = 50
    for line in data:
        direction = line[0]
        num_rot = int(line[1:]) % 100
        full_rot = int(int(line[1:]) / 100)
        if direction == 'L':
            temp = pos - num_rot
            temp_pos = pos
            pos = ((pos - num_rot) % 100)
            if temp <= 0 and temp_pos != 0:
                res = res + full_rot + 1
            else:
                res += full_rot
        else:
            pass_zero = int((pos + num_rot) / 100)
            temp_pos = 0
            pos = abs(pos + num_rot) % 100
            if pass_zero >= 1:
                res = res + full_rot + 1
            else:
                res += full_rot
    return res



if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1:", part1(data[0]))
    print("Part 2:", part2(data[0]))
    # 6941 is too high
    # 5829 is too low
    # 6372 is too low
