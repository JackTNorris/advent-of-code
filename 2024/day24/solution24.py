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

def part2():
    # know we're dealing with a ripple carry adder based on reddit + some help
    # diagram here: https://media.geeksforgeeks.org/wp-content/uploads/3-57.png

    start_values, connections = aoc_utils.return_array_from_file('input.txt')
    known_values = {}
    rely_on = defaultdict(lambda: [])
    for item in start_values:
        name, val = item.split(': ')
        known_values[name] = int(val)
    
    # maps all "wires" to the expressions it is a part of
    conn_dict = defaultdict(lambda: set())

    for conn in connections:
        expression, assignment = conn.split(' -> ')
        n1, op, n2 = expression.split(' ')
        conn_dict[n1].add(conn)
        conn_dict[n2].add(conn)
        if assignment.find('z') > -1 and expression.find('XOR') < 0:
            print('problem with ', assignment)

        
    
    # num input outputs
    carry_in = None
    carry_out = None

    
    for i in range(45):
        # test x y interaction
        x_input = "x{:02d}".format(i)
        y_input = "y{:02d}".format(i)
        xys = set(conn_dict[x_input] & conn_dict[y_input])
        if len(xys) != 2:
            print('fishiness with x', i)
        first_xor_output = None
        first_and_output = None
        for conn in xys:
            if conn.find("XOR") > -1:
                expression, assignment = conn.split(' -> ')
                known_values[assignment] = evaluate(expression, known_values)
                first_xor_output = assignment
            if conn.find("AND") > -1:
                expression, assignment = conn.split(' -> ')
                known_values[assignment] = evaluate(expression, known_values)
                first_and_output = assignment
            known_values[assignment] = evaluate(expression, known_values)
        if first_xor_output == None or first_and_output == None:
            # checked, no issues here
            print('Problem with x or y: ',  i)
        
        # test that the AND output of XY is ORD'd and only used once:
        temp = conn_dict[first_and_output]
        if len(temp) > 1:
            print("Something is possibly wrong with: ", first_and_output)
        
        
        # test that the XOR output of XY is somehow XOR'd into Zi (one time)
        temp = list(filter(lambda x: x.find('XOR') >= 0 and x.find("z{:02d}".format(i)) >= 0, conn_dict[first_xor_output]))
        if len(temp) != 1:
            print("Something is possibly wrong with: ", first_xor_output)
        """
        # test that the XOR output of XY is AND'd with something (only once):
        temp = list(filter(lambda x: x.find('AND') >= 0, conn_dict[first_xor_output]))
        if len(temp) != 1:
            print("Something is possibly wrong with: ", first_xor_output)
        """
        

        

print("Part 2: ", part2())