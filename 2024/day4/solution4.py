import sys, os
import numpy as np
from collections import defaultdict
sys.path.append('../../')
import aoc_utils

def part1():
    word_search = aoc_utils.return_array_from_file('./input.txt')[0]
    print(word_search)
    rows, columns = len(word_search), len(word_search[0])

    def check_xmas(row, col, word_index, row_delt, col_delt):
        if row >= rows or col >= columns or row < 0 or col < 0:
            return False
        elif word_search[row][col] != "XMAS"[word_index]:
            return False
        elif word_index == len("XMAS") - 1:
            print(f"Found XMAS at ({row}, {col}) moving ({row_delt}, {col_delt})")
            return True
        else:
            return check_xmas(row + row_delt, col + col_delt, word_index + 1, row_delt, col_delt)

    count = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            # rook behavior
            count += check_xmas(i, j, 0, 1, 0) + check_xmas(i, j, 0, -1, 0) + check_xmas(i, j, 0, 0, 1) + check_xmas(i, j, 0, 0, -1)
            # bishop behavior
            count += check_xmas(i, j, 0, -1, 1) + check_xmas(i, j, 0, -1, -1) + check_xmas(i, j, 0, 1, -1) + check_xmas(i, j, 0, 1, 1)
    return count


def part2():
    word_search = aoc_utils.return_array_from_file('./input.txt')[0]
    print(word_search)
    rows, columns = len(word_search), len(word_search[0])

    def check_mas(row_a, col_a):
        if row_a >= (rows) - 1 or col_a >= (columns) - 1 or row_a == 0 or col_a == 0:
            return False
        tl_corner = [row_a - 1, col_a - 1]
        tr_corner = [row_a - 1, col_a + 1]
        bl_corner = [row_a + 1, col_a - 1]
        br_corner = [row_a + 1, col_a + 1]

        temp1 = word_search[tl_corner[0]][tl_corner[1]] + 'A' + word_search[br_corner[0]][br_corner[1]]
        temp2 = word_search[tr_corner[0]][tr_corner[1]] + 'A' + word_search[bl_corner[0]][bl_corner[1]]
        if (temp1 == 'MAS' or temp1[::-1] == 'MAS') and (temp2 == 'MAS' or temp2[::-1] == 'MAS'):
            return True
        return False
    count = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[0])):
            if word_search[i][j] == 'A':
                count += check_mas(i, j)
            
    return count
        

print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))


