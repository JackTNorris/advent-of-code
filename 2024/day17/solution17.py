import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy

def format_output(o):
    return ','.join( list(map(lambda x: str(x), o))) 

def part1():
    register_states, program = aoc_utils.return_array_from_file('./input.txt')
    register_a, register_b, register_c = list(map(lambda x: int(x.split(': ')[1]), register_states))
    program = program[0].split(': ')[1]
    program = list(map(lambda x: int(x), program.split(',')))
    output = []
    instruction_pointer = 0
    did_jump = False
    def get_combo(operand):
        nonlocal register_a, register_b, register_c
        if operand <= 3:
            return operand
        else:
            if operand == 4:
                return register_a
            if operand == 5:
                return register_b
            if operand == 6:
                return register_c
        return -1

    def perform_step(opcode, operand):
        nonlocal register_a, register_b, register_c, instruction_pointer
        if opcode == 0:
            register_a = int(register_a / (2**get_combo(operand)))
        elif opcode == 1:
            register_b = register_b^operand
        elif opcode == 2:
            register_b = get_combo(operand) % 8
        elif opcode == 3:
            if register_a != 0:
                instruction_pointer = operand
        elif opcode == 4:
            register_b = register_b ^ register_c
        elif opcode == 5:
            output.append(get_combo(operand) % 8)
        elif opcode == 6:
            register_b = int(register_a / (2**get_combo(operand)))
        elif opcode == 7:
            register_c = int(register_a / (2**get_combo(operand)))
    
    while instruction_pointer < len(program):
        opcode, operand = program[instruction_pointer], program[instruction_pointer + 1]
        instruction_pointer += 2
        perform_step(opcode, operand)

    return format_output(output)

# note that this is slightly different person to person (code is polymorphic, but function should be the same)
def run_program(a):
    b, c = 0, 0
    output = []
    while a != 0:
        b = a % 8
        b = b ^ 1
        c = int(a / (2 ** b))
        a = int(a / (2**3))
        b = b ^ c
        b = b ^ 6
        output.append(b % 8)
    return output

def octal_to_decimal(oct_str):
    fin_sum = 0
    base = 0
    for i in range(len(oct_str) - 1, -1, -1):
        fin_sum += int(oct_str[i]) * (8 ** base)
        base += 1
    return fin_sum


def find_a(o_string, pos, program, solution):
    if run_program(octal_to_decimal(o_string))[::-1] == program:
        solution[0] = min(solution[0], octal_to_decimal(o_string))
    else:
        for i in range(pos, 16):
            for j in range(8):
                temp_octal = list(o_string[:])
                temp_octal[i] = str(j)
                temp_octal = "".join(temp_octal)
                res = run_program(octal_to_decimal(temp_octal))
                res.reverse()
                if len(res) > 0 and i < len(res) and res[i] == program[i]:
                    find_a(temp_octal, i + 1, program, solution)

def part2():
    program = [2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0]
    program.reverse()
    solution = [float('inf')]
    find_a("0000000000000000", 0, program, solution)
    return solution[0]

print("Part 2: ", part2())

