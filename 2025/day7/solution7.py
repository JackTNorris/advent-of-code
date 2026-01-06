#!/usr/bin/env python3
from typing import List
import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict

# no such thing as ^^, ^ aren't on edges either
def part1(data):
    res = 0
    num_rows, num_cols = len(data), len(data[0])
    print(num_rows)
    print(num_cols)
    data = list(map(list, data))
    for i in range(1, num_rows):
        above_row = data[i-1]
        for j in range(num_cols):
            if data[i][j] == '^':
                if above_row[j] == '|':
                    data[i][j - 1] = '|'
                    data[i][j + 1] = '|'
                    res += 1
            elif above_row[j] == 'S':
                data[i][j] = '|'
            elif above_row[j] == '|':
                data[i][j] = '|'
    return res

    

def part2(data: List[str]):
    num_rows, num_cols = len(data), len(data[0])
    data = list(map(list, data))
    for i in range(1, num_rows):
        above_row = data[i-1]
        for j in range(num_cols):
            if data[i][j] == '^':
                if above_row[j] == '|':
                    data[i][j - 1] = '|'
                    data[i][j + 1] = '|'
            elif above_row[j] == 'S':
                data[i][j] = '|'
            elif above_row[j] == '|':
                data[i][j] = '|'
    res = 0
    from functools import lru_cache
    @lru_cache
    def dfs(i, j):
        nonlocal res
        if i == num_rows - 1:
            return 1
        elif data[i][j] == '.':
            return 0
        elif data[i][j] == '|':
            return dfs(i +1, j)
        elif data[i][j] == '^':
            return dfs(i + 1, j + 1) + dfs(i + 1, j - 1)
    for j in range(len(data[0])):
        if data[0][j] == 'S':
            res = dfs(1, j)
    return res
        

if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1: ", part1(data[0]))
    print("Part 2: ", part2(data[0]))
