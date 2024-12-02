import sys, os
import numpy as np
from collections import defaultdict

sys.path.append('../../')
import aoc_utils


def is_safe(nums):
    state = ''
    valid = True
    errant_index = -1
    for n in range(1, len(nums)):
        temp = nums[n - 1] - nums[n]
        if not (abs(temp) > 0 and abs(temp) < 4):
            valid = False
            errant_index = n
            break
        elif n == 1:
            state = 'dec' if temp > 0 else 'inc'
        else:
            temp2 = 'dec' if temp > 0 else 'inc'
            if state != temp2:
                valid = False
                errant_index = n
                break
    return [1,-1] if valid else [0, errant_index]

def part1():
    data = aoc_utils.return_array_from_file('input.txt')[0]
    num_safe = 0
    for line in data:
        nums = list(map(lambda x: int(x), line.split(' ')))
        num_safe += is_safe(nums)[0]
    return num_safe


def part2():
    def check_safety_with_padding(arr, num_removed):
        safe = is_safe(arr)
        if not safe[0]:
            if num_removed == 1:
                return False
            else:
                new_arrs = []
                for i in range(len(arr)):
                    t = []
                    for j in range(len(arr)):
                        if i != j:
                            t.append(arr[j])
                    new_arrs.append(t)
                temp = False
                for a in new_arrs:
                    temp = temp or check_safety_with_padding(a, num_removed + 1)
                    if temp == True:
                        return True
                return temp
        return True

    data = aoc_utils.return_array_from_file('input.txt')[0]
    num_safe = 0
    for line in data:
        nums = list(map(lambda x: int(x), line.split(' ')))
        safe = check_safety_with_padding(nums, 0)
        if safe:
            num_safe += 1

    return num_safe

print('Part 2: ', part2())
            



        
        