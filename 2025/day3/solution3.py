#!/usr/bin/env python3

import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict

# hacky as crap, but oiko
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

# looking to make the biggest 12 digit number from the input
def part2(data: List[str]):
    res = 0
    # gets highest number in given inclusive range

    ghr_memo = {}
    def get_highest_range(arr, start, num_ahead):
        if ("".join(map(str, arr)), start, num_ahead) in ghr_memo:
            return ghr_memo[("".join(map(str, arr)), start, num_ahead)]
        max_val = -1
        loc_res = []
        for i in range(start, len(arr) + 1 - num_ahead):
            max_val = max(max_val, arr[i])
        for i in range(start, len(arr) + 1 - num_ahead):
            if arr[i] == max_val:
                loc_res.append(i)
        ghr_memo[("".join(map(str, arr)), start, num_ahead)] = loc_res
        return loc_res
    
    gln_memo = {}
    def get_largest_number(arr, start, num_ahead):
        if ("".join(map(str, arr)), start, num_ahead) in gln_memo:
            return gln_memo[("".join(map(str, arr)), start, num_ahead)]
        if num_ahead == 0:
            return ""
        locs = get_highest_range(arr, start, num_ahead)
        best_res = ""
        for loc in locs:
            candidate = str(arr[loc]) + get_largest_number(arr, loc + 1, num_ahead - 1)
            if candidate > best_res:
                best_res = candidate
        gln_memo[("".join(map(str, arr)), start, num_ahead)] = best_res
        return best_res
    
    for i in range(len(data)):
        case = data[i]
        temp_case = list(map(lambda x: int(x), case))
        z = int(get_largest_number(temp_case, 0, 12))
        res += z
        print('case ', i)
    return res
        

"""thinking space"""
"""
- break it down into sub problems
- for a given range, find highest number with at least y digits in front of it
- follow all possibilities and find the highest
"""

if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    #print("Part 1: ", part1(data[0]))
    print("Part 2: ", part2(data[0]))