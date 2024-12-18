import sys, os
from collections import defaultdict
import regex as re
sys.path.append('../../')
import aoc_utils
from typing import List, Tuple, Set, Dict
import heapq




def dir_from_string(s):
    if s == 'w':
        return (0, -1)
    elif s == 'e':
        return (0, 1)
    elif s == 'n':
        return (-1, 0)
    elif s == 's':
        return (1, 0)
    else:
        return (-1, -1)

def part1():
    maze = aoc_utils.return_array_from_file('./input.txt')[0]
    directions = ['n', 'e', 's', 'w']
    dijkstra_graph = []
    start_pos = None
    end_pos = None
    for row in range(len(maze)):
        temp = []
        for col in range(len(maze[0])):
            temp2 = []
            if maze[row][col] == 'E':
                end_pos = (row, col)
            for d in directions:
                temp2.append(float('inf'))
                if d == 'e' and maze[row][col] == 'S':
                    temp2.append(0)
                    start_pos = (row, col, 'e')
            temp.append(temp2)
        dijkstra_graph.append(temp)

    to_visit = [(0, start_pos)]
    heapq.heapify(to_visit) # not necessary
    while len(to_visit) > 0:
        curr_dist, item = heapq.heappop(to_visit)
        curr_dir_enum = directions.index(item[2])
        if curr_dist > dijkstra_graph[item[0]][item[1]][curr_dir_enum]:
            continue
        elif maze[item[0]][item[1]] == '#':
            continue
        # check
        move = dir_from_string(item[2])

        temp = [item[0] + move[0],item[1] + move[1]]
        if dijkstra_graph[temp[0]][temp[1]][curr_dir_enum] > curr_dist + 1:
            dijkstra_graph[temp[0]][temp[1]][curr_dir_enum] = curr_dist + 1
            heapq.heappush(to_visit, (curr_dist + 1, (temp[0], temp[1], item[2])))
        # 90 degree shifts
        if dijkstra_graph[item[0]][item[1]][(curr_dir_enum + 1) % 4] > curr_dist + 1000:
            dijkstra_graph[item[0]][item[1]][(curr_dir_enum + 1) % 4] = curr_dist + 1000
            heapq.heappush(to_visit, (curr_dist + 1000, (item[0], item[1], directions[(curr_dir_enum + 1) % 4])))
        if dijkstra_graph[item[0]][item[1]][(curr_dir_enum + 3) % 4] > curr_dist + 1000:
            dijkstra_graph[item[0]][item[1]][(curr_dir_enum + 3) % 4] = curr_dist + 1000
            heapq.heappush(to_visit, (curr_dist + 1000, (item[0], item[1], directions[(curr_dir_enum + 3) % 4])))
        # 180 degree shift
        if dijkstra_graph[item[0]][item[1]][(curr_dir_enum + 2) % 4] > curr_dist + 2000:
            dijkstra_graph[item[0]][item[1]][(curr_dir_enum + 2) % 4] = curr_dist + 2000
            heapq.heappush(to_visit, (curr_dist + 2000, (item[0], item[1], directions[(curr_dir_enum + 2) % 4])))
    return min(dijkstra_graph[end_pos[0]][end_pos[1]])
print(part1())
