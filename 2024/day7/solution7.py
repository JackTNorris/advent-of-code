import sys, os
import numpy as np
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List


def get_calc_array(cal_string: str) -> List[str]:
    nums = re.split("[+,*]", cal_string)
    ops = list(filter(lambda x: x != '', re.split("[0-9]+", cal_string)))
    temp = []
    i = 0
    while len(nums) > 0 or len(ops) > 0:
        if i % 2 == 0:
            temp.append(nums.pop(0))
        else:
            temp.append(ops.pop(0))
        i += 1
    return temp

        

# want to do this without help
def calculate(cal_string: str):
    t_string = cal_string
    c_arr = get_calc_array(t_string)
    while(t_string.find('*') > 0):
        try:
            temp = c_arr.index('*')
            new_thang_string = c_arr[temp -  1] + c_arr[temp] + c_arr[temp +  1]
            new_thang = int(c_arr[temp -  1]) * int(c_arr[temp +  1])
            t_string = t_string.replace(new_thang_string, str(new_thang))
            c_arr = get_calc_array(t_string)
        except:
            print("shouldn't get here")
    add_events = list(map(lambda x: int(x), re.split('[+]', t_string)))
    return sum(add_events)


def calculate_dumb(cal_string: str):
    nums = re.split("[+,*,|]", cal_string)
    ops = list(filter(lambda x: x != '', re.split("[0-9]+", cal_string)))
    res = 0
    while len(ops) > 0:
        op = ops.pop(0)
        n1, n2 = nums.pop(0), nums.pop(0)
        if op == '*':
            t = int(n1) * int(n2)
        elif op == '|':
            t = int(str(n1) + str(n2))
        else:
            t = int(n1) + int(n2)
        res = t
        nums.insert(0, t)
    return res

def generate_possible_plus_mult(size, curr_str, possibilities: List):
    if len(curr_str) == size:
        possibilities.append(curr_str)
    else:
        generate_possible_plus_mult(size, curr_str + "*", possibilities)
        generate_possible_plus_mult(size, curr_str + "+", possibilities)

def generate_possible_plus_mult_union(size, curr_str, possibilities: List):
    if len(curr_str) == size:
        possibilities.append(curr_str)
    else:
        generate_possible_plus_mult_union(size, curr_str + "*", possibilities)
        generate_possible_plus_mult_union(size, curr_str + "+", possibilities)
        generate_possible_plus_mult_union(size, curr_str + "|", possibilities)


def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0];
    res = 0
    for line in data:
        broken = line.split(': ')
        des_res = int(broken[0])
        blank_equation = broken[1]
        possible_plus_minus = []
        num_spaces = len(blank_equation) - len(blank_equation.replace(" ", ""))
        generate_possible_plus_mult(num_spaces, "", possible_plus_minus)
        for symstr in possible_plus_minus:
            nums = blank_equation.split(' ')
            ops = list(symstr)
            calc_string = ""
            i = 0
            while len(nums) > 0 or len(ops) > 0:
                if i % 2 == 0:
                    calc_string += (nums.pop(0))
                else:
                    calc_string += (ops.pop(0))
                i += 1
            if calculate_dumb(calc_string) == des_res:
                res += des_res
                break
    return res

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')[0];
    res = 0
    for line in data:
        broken = line.split(': ')
        des_res = int(broken[0])
        blank_equation = broken[1]
        possible_plus_minus = []
        num_spaces = len(blank_equation) - len(blank_equation.replace(" ", ""))
        generate_possible_plus_mult_union(num_spaces, "", possible_plus_minus)
        for symstr in possible_plus_minus:
            nums = blank_equation.split(' ')
            ops = list(symstr)
            calc_string = ""
            i = 0
            while len(nums) > 0 or len(ops) > 0:
                if i % 2 == 0:
                    calc_string += (nums.pop(0))
                else:
                    calc_string += (ops.pop(0))
                i += 1
            if calculate_dumb(calc_string) == des_res:
                res += des_res
                break
    return res

print("Part 2: ", part2())