import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy
from functools import cmp_to_key

def part1():
    data = aoc_utils.return_array_from_file('input.txt')[0]
    graph = defaultdict(lambda: [])
    # construct graph
    for pair in data:
        p1, p2 = pair.split('-')
        graph[p1].append(p2)
        graph[p2].append(p1)
    print('crafted graph')
    def is_part_of_cycle_three(node, graph, curr_path, cycles):
        curr_path.append(node)
        if len(curr_path) > 3:
            if curr_path[0] == curr_path[3]:
                curr_path = curr_path[:3]
                curr_path.sort()
                if curr_path not in cycles:
                    cycles.append((curr_path))
                return True
            return False
        to_visit = list(graph[node])
        temp = False
        for v in to_visit:
            if v == curr_path[0] and len(curr_path) == 3:
                curr_path.sort()
                if curr_path not in cycles:
                    cycles.append((curr_path))
            temp = temp or is_part_of_cycle_three(v, graph, curr_path[:], cycles)
        return []


    final_cycles = set()

    for item in graph.keys():
        cycles = []
        is_part_of_cycle_three(item, graph, [], cycles)
        for c in cycles:
            final_cycles.add("".join(c))
    
    res = 0
    for cycle in final_cycles:
        c1 = cycle[0:2]
        c2 = cycle[2:4]
        c3 = cycle[4:6]
        if c1.find('t') == 0 or c2.find('t') == 0 or c3.find('t') == 0:
            res += 1
    return res

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R.union({v}),
            P.intersection(graph[v]),
            X.intersection(graph[v]),
            graph
        )
        X.add(v)


def part2():
    data = aoc_utils.return_array_from_file('input.txt')[0]
    edges = []
    curr_max_size = 0
    # construct graph
    for pair in data:
        p1, p2 = pair.split('-')
        edges.append((p1, p2))

    graph = {i[0]: set() for i in edges}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    graph = {key: set(graph[key]) for key in graph}
    all_cliques = list(bron_kerbosch(set(), set(graph.keys()), set(), graph))
    if all_cliques:
        max_clique_size = max(len(clique) for clique in all_cliques)
    else:
        max_clique_size = -1
    temp = list(list(filter(lambda x: len(x) == max_clique_size, all_cliques))[0])
    temp.sort()
    print(",".join(temp))
    

    
        

print("Part1: ", part2())