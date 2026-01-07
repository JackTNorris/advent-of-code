#!/usr/bin/env python3
from typing import List
import sys
sys.path.append('../../')
import aoc_utils
from typing import List
from collections import defaultdict
import math

# no such thing as ^^, ^ aren't on edges either
def part1(data):
    res = 0
    distances = []
    # constructing our edged graph
    for i in range(len(data)):
        (x1, y1, z1) = map(int, data[i].split(','))
        for j in range(i + 1, len(data)):
            (x2, y2, z2) = map(int, data[j].split(','))
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
            distances.append((data[i], data[j], dist))
            
    distances = sorted(distances, key=lambda x: x[2])
    
    print("made initial graph")
    # reducing our graph
    conn_graph = defaultdict(set)

    for i in range(1000):
        d = distances[i]
        conn_graph[d[0]].add(d[0])
        conn_graph[d[1]].add(d[1])        
        conn_graph[d[0]].update(conn_graph[d[1]])
        conn_graph[d[1]].update(conn_graph[d[0]])
        for c in conn_graph[d[0]]:
           conn_graph[c].update(conn_graph[d[0]])
        for c in conn_graph[d[1]]:
           conn_graph[c].update(conn_graph[d[1]])

    print("made connection graph")
    sol = []
    print(conn_graph)
    for c in conn_graph.keys():
        t = list(conn_graph[c])
        t.sort()
        sol.append(tuple(t))
    sol = set(sol)
    sol = list(sol)
    sol = sorted(sol, key=len)
    return len(sol[-1]) * len(sol[-2]) * len(sol[-3])

    

def part2(data: List[str]):
    num_rows, num_cols = len(data), len(data[0])
    res = 0
    return res
        

if __name__ == "__main__":
    data = aoc_utils.return_array_from_file('input.txt')
    print("Part 1: ", part1(data[0]))
    # print("Part 2: ", part2(data[0]))
