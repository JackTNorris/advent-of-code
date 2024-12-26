import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy
from functools import cmp_to_key

def evaluate(expression, graph):
    n1, op, n2 = expression.split(' ')
    if op == 'AND':
        return graph[n1] and graph[n2]
    if op == 'OR': 
        return graph[n1] or graph[n2]
    if op == 'XOR':
        return graph[n1] ^ graph[n2]
    raise Exception("Invalid operation")


def part1():
    start_values, connections = aoc_utils.return_array_from_file('input.txt')
    known_values = {}
    rely_on = defaultdict(lambda: [])
    for item in start_values:
        name, val = item.split(': ')
        known_values[name] = int(val)
    while len(known_values.keys()) - len(start_values) != len(connections):
        for conn in connections:
            cant_handle = False
            expression, assignment = conn.split(' -> ')
            n1, op, n2 = expression.split(' ')
            if n1 not in known_values:
                cant_handle = True
                rely_on[n1] = expression
            if n2 not in known_values:
                rely_on[n2] = expression
                cant_handle = True
            if not cant_handle:
                known_values[assignment] = evaluate(expression, known_values)
    
    # no funky business with inputs so this works
    z_outputs = list(filter(lambda x: x.find('z') == 0, known_values.keys()))
    z_outputs.sort()
    dec_rep = 0
    for i in range(len(z_outputs)):
        dec_rep += known_values[z_outputs[i]] * 2**i
    return dec_rep

print(part1())