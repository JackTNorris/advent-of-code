#!/usr/bin/env python3
import sys
sys.path.append('../../')
import aoc_utils
from typing import List


def part1(data: List[str]):
    res = 0
    for case in data:
        min_val, max_val = map(int, case.split('-'))
        if len(str(min_val)) % 2 == 1 and len(str(max_val)) % 2 == 1:
            res += 0
        else:
            for i in range(min_val, max_val + 1):
                str_num = str(i)
                if len(str_num) % 2 == 0 and str_num[0:len(str_num)//2] == str_num[len(str_num)//2:]:
                    res += i
    return res


def part2(data: List[str]):
    res = 0
    def is_valid(s):
        # sliding window i
        for i in range(1, len(s) // 2 + 1):
            is_good = True
            to_match = s[0:i]
            if len(s) % len(to_match) == 0:
                for j in range(int(len(s) / len(to_match))):
                    if s[j*len(to_match):(j+1)*len(to_match)] != to_match:
                        is_good = False
                        break
            else:
                is_good = False
            if is_good:
                return True
    for case in data:
        min_val, max_val = map(int, case.split('-'))
        for i in range(min_val, max_val + 1):
            str_num = str(i)
            if is_valid(str_num):
                res += i
    return res


if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    #print("".join(data[0]).split(','))
    print("Part 1: ", part1("".join(data[0]).split(',')))
    print("Part 2: ", part2("".join(data[0]).split(',')))
