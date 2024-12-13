import sys, os
import numpy as np
from collections import defaultdict
import math
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict

def get_perimeter(region):
    region_set = set(region)
    perimeter = 0
    for element in region_set:
        above = (element[0] - 1, element[1])
        below = (element[0] + 1, element[1])
        right = (element[0], element[1] + 1)
        left = (element[0], element[1] - 1)
        perimeter += (not (above in region_set)) +(not (below in region_set )) + (not (left in region_set )) + (not (right in region_set ))
    return perimeter

def get_sides(region):
    region_set = set(region)
    horizontal_edges = set()
    vertical_edges = set()
    # extract edges, using fractional representations for edges
    for element in region_set:
        above = (element[0] - 1, element[1])
        below = (element[0] + 1, element[1])
        right = (element[0], element[1] + 1)
        left = (element[0], element[1] - 1)
        if above not in region_set:
            horizontal_edges.add((element[0] - 0.5, element[1]))
        if below not in region_set:
            horizontal_edges.add((element[0] + 0.5, element[1]))
        if right not in region_set:
            vertical_edges.add((element[0], element[1] + 0.5))
        if left not in region_set:
            vertical_edges.add((element[0], element[1] - 0.5))

    visited_horizontal = set()
    visited_vertical = set()
    
    def get_horizontal_edges(curr_edge, edge_list):
        if curr_edge in horizontal_edges:
            if curr_edge not in visited_horizontal:
                visited_horizontal.add(curr_edge)
                edge_list.append(curr_edge)
                get_horizontal_edges((curr_edge[0], curr_edge[1] + 1), edge_list)
                get_horizontal_edges((curr_edge[0], curr_edge[1] - 1), edge_list)

    def get_vertical_edges(curr_edge, edge_list):
        if curr_edge in vertical_edges:
            if curr_edge not in visited_vertical:
                visited_vertical.add(curr_edge)
                edge_list.append(curr_edge)
                get_vertical_edges((curr_edge[0] + 1, curr_edge[1]), edge_list)
                get_vertical_edges((curr_edge[0] - 1, curr_edge[1]), edge_list)

    num_edges = 0
    horizontal_edge_list = []
    vertical_edge_list = []
    for hor_edge in horizontal_edges:
        hor_edge_parts = []
        get_horizontal_edges(hor_edge, hor_edge_parts)
        if len(hor_edge_parts) > 0:
            horizontal_edge_list.append((hor_edge_parts))
            #print("HORIZONTAL EDGE: ", hor_edge_parts)
            num_edges += 1
    
    for ver_edge in vertical_edges:
        ver_edge_parts = []
        get_vertical_edges(ver_edge, ver_edge_parts)
        if len(ver_edge_parts) > 0:
            vertical_edge_list.append((ver_edge_parts))
            #print("VERTICAL EDGE: ", ver_edge_parts)
            num_edges += 1

    # detect junctions
    num_junctions = 0
    for h_group in horizontal_edge_list:
        h_group = sorted(h_group, key=lambda x: x[1])
        #print(h_group)
        for i in range(len(h_group) - 1):
            op1 = (h_group[i][0] + 0.5, h_group[i][1] + 0.5)
            op2 = (h_group[i][0] - 0.5, h_group[i][1] + 0.5)
            for v_group in vertical_edge_list:
                for v in v_group:
                    if op1[0] == v[0] and op1[1] == v[1]:
                        num_junctions += 1
                    if op2[0] == v[0] and op2[1] == v[1]:
                        num_junctions += 1

            
    print("NUM JUNCTIONS: ", num_junctions)


    

         
    #print("NUM EDGES: ", num_edges)

    return num_edges + num_junctions



        

def part1():
    data = aoc_utils.return_array_from_file('./input.txt')[0]
    num_rows = len(data)
    num_cols = len(data[0])
    def flood(flood_char, visited: Set[Tuple], curr_pos: Tuple, region: List[Tuple]):
        if curr_pos[0] >= num_rows or curr_pos[1] >= num_cols or curr_pos[0] < 0 or curr_pos[1] < 0:
            return
        else:
            if data[curr_pos[0]][curr_pos[1]] == flood_char and curr_pos not in visited:
                visited.add(curr_pos)
                region.append(curr_pos)
                flood(flood_char, visited, (curr_pos[0] + 1, curr_pos[1]), region)
                flood(flood_char, visited, (curr_pos[0] - 1, curr_pos[1]), region)
                flood(flood_char, visited, (curr_pos[0], curr_pos[1] + 1), region)
                flood(flood_char, visited, (curr_pos[0], curr_pos[1] - 1), region)
            else:
                return

    regions = []
    visited = set()
    
    for row in range(len(data)):
        for col in range(len(data[0])):
            region = []
            if (row, col) not in visited:
                flood(data[row][col], visited, (row, col), region)
                regions.append(region)
    res = 0
    for r in regions:
        res += len(r) * get_perimeter(r)

    return res

def part2():
    data = aoc_utils.return_array_from_file('./input.txt')[0]
    num_rows = len(data)
    num_cols = len(data[0])
    def flood(flood_char, visited: Set[Tuple], curr_pos: Tuple, region: List[Tuple]):
        if curr_pos[0] >= num_rows or curr_pos[1] >= num_cols or curr_pos[0] < 0 or curr_pos[1] < 0:
            return
        else:
            if data[curr_pos[0]][curr_pos[1]] == flood_char and curr_pos not in visited:
                visited.add(curr_pos)
                region.append(curr_pos)
                flood(flood_char, visited, (curr_pos[0] + 1, curr_pos[1]), region)
                flood(flood_char, visited, (curr_pos[0] - 1, curr_pos[1]), region)
                flood(flood_char, visited, (curr_pos[0], curr_pos[1] + 1), region)
                flood(flood_char, visited, (curr_pos[0], curr_pos[1] - 1), region)
            else:
                return

    regions = []
    visited = set()
    
    for row in range(len(data)):
        for col in range(len(data[0])):
            region = []
            if (row, col) not in visited:
                flood(data[row][col], visited, (row, col), region)
                regions.append(region)
    res = 0
    for r in regions:
        print(len(r))
        res += len(r) * get_sides(r)

    return res


print("Part 2: ", part2())
