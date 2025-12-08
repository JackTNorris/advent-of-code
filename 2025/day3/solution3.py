#!/usr/bin/env python3

import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict

def part1(data: List[str]):
    res = 0
    for case in data:
        num_indices = defaultdict(list)
        for i in range(len(case)):
            num_indices[int(case[i])].append(i)
        found = False
        for j in range(9, -1, -1):
            for z in range(len(num_indices[j])):
                for u in range(9, -1, -1):
                    for v in range(len(num_indices[u])):
                        if num_indices[j][z] < num_indices[u][v]:
                            res += j * 10 + u
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        
    return res
                


        
        
    # TODO: implement Day 3 part 1
    return None


def part2(data: List[str]):
    # TODO: implement Day 3 part 2
    return None


if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1: ", part1(data[0]))
