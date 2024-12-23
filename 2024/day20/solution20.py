import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq
from copy import copy, deepcopy

n, s, e, w = (-1, 0), (1, 0), (0,- 1), (0, 1)
directions = [n, s, e, w]

def navigate_dijkstra(start_pos, dijkstra_navigator, track):
    global directions
    to_visit = [(0, start_pos)]
    heapq.heapify(to_visit) # not necessary
    while len(to_visit) > 0:
        curr_dist, item = heapq.heappop(to_visit)
        if curr_dist > dijkstra_navigator[item[0]][item[1]]:
            continue
        elif item[0] >= len(dijkstra_navigator) or item[0] < 0 or item[1] >= len(dijkstra_navigator[0]) or item[1] < 0:
            continue
        elif track[item[0]][item[1]] == '#':
            continue
        for d in directions:
            temp = [item[0] + d[0],item[1] + d[1]]
            if dijkstra_navigator[temp[0]][temp[1]] > curr_dist + 1:
                dijkstra_navigator[temp[0]][temp[1]] = curr_dist + 1
                heapq.heappush(to_visit, (curr_dist + 1, (temp[0], temp[1])))



def part1():
    save_me = 100
    track = list(map(lambda x: list(x), aoc_utils.return_array_from_file('input.txt')[0]))
    start_pos, end_pos = None, None
    dijkstra_navigator = []
    walkable = []
    for row in range(len(track)):
        temp = []
        for col in range(len(track[0])):
            if track[row][col] == 'S':
                temp.append(0)
                start_pos = (row, col)
                walkable.append((row, col))
            elif track[row][col] == 'E':
                walkable.append((row, col))
                temp.append(float('inf'))
                end_pos = (row, col)
            else:
                if track[row][col] != '#':
                    walkable.append((row, col))
                temp.append(float('inf'))
        dijkstra_navigator.append(temp)

    navigate_dijkstra(start_pos, dijkstra_navigator, track)
    res = 0
    all_dirs = [(-2, 0), (2, 0), (0,- 2), (0, 2), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for walk in walkable:
        for d in all_dirs:
            temp = (walk[0] + d[0], walk[1] + d[1])
            if temp[0] >= 0 and temp[0] < len(track) and temp[1] >= 0 and temp[1] < len(track[0]):
                if track[temp[0]][temp[1]] == '.' or track[temp[0]][temp[1]] == 'E' :
                    if dijkstra_navigator[temp[0]][temp[1]] - dijkstra_navigator[walk[0]][walk[1]] >= save_me + 2:
                        res += 1
    return res
    
def manhattan_vectors(max_distance=20):
    vectors = []
    for x in range(-max_distance, max_distance + 1):
        for y in range(-max_distance, max_distance + 1):
                if abs(x) + abs(y) <= max_distance:
                    vectors.append((x, y))
    return vectors

def man_distance(vector):
    return abs(vector[0]) + abs(vector[1])

def part2():
    save_me = 100
    track = list(map(lambda x: list(x), aoc_utils.return_array_from_file('input.txt')[0]))
    start_pos, end_pos = None, None
    dijkstra_navigator = []
    walkable = []
    for row in range(len(track)):
        temp = []
        for col in range(len(track[0])):
            if track[row][col] == 'S':
                temp.append(0)
                start_pos = (row, col)
                walkable.append((row, col))
            elif track[row][col] == 'E':
                walkable.append((row, col))
                temp.append(float('inf'))
                end_pos = (row, col)
            else:
                if track[row][col] != '#':
                    walkable.append((row, col))
                temp.append(float('inf'))
        dijkstra_navigator.append(temp)

    my_temp = []
    navigate_dijkstra(start_pos, dijkstra_navigator, track)
    res = 0
    all_dirs = manhattan_vectors(20)
    for walk in walkable:
        for d in all_dirs:
            temp = (walk[0] + d[0], walk[1] + d[1])
            if temp[0] >= 0 and temp[0] < len(track) and temp[1] >= 0 and temp[1] < len(track[0]):
                if track[temp[0]][temp[1]] != '#':
                    if dijkstra_navigator[temp[0]][temp[1]] - dijkstra_navigator[walk[0]][walk[1]] >= save_me + man_distance(d):
                        my_temp.append(dijkstra_navigator[temp[0]][temp[1]] - dijkstra_navigator[walk[0]][walk[1]] - man_distance(d))
                        res += 1
    my_temp.sort()
    g = defaultdict(lambda: 0)
    for item in my_temp:
        g[item] += 1
    for item in g.keys():
        print("Number of: " + str(item) + ": ", g[item])
    return res
    


print(part2())