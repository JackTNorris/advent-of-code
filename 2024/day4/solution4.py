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

        

#print("Part 1: " + str(part1()))
print("Part 1: " + str(part1()))


