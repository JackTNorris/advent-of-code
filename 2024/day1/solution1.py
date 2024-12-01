import sys, os
import numpy as np
from collections import defaultdict

sys.path.append('../../')
import aoc_utils


def part1():
    lines = aoc_utils.return_array_from_file('./part-1-input.txt')[0]
    left = np.array(list(map(lambda x: int(x.split("   ")[0]), lines)))
    right = np.array(list(map(lambda x: int(x.split("   ")[1]), lines)))

    left.sort()
    right.sort()

    dist = abs(left - right)

    return (sum(dist))


def part2():
    lines = aoc_utils.return_array_from_file('./part-1-input.txt')[0]
    left = (list(map(lambda x: int(x.split("   ")[0]), lines)))
    right = (list(map(lambda x: int(x.split("   ")[1]), lines)))

    right_map = defaultdict(lambda: 0)
    for r in right:
        right_map[r] += 1

    sim_score = 0
    for l in left:
        sim_score += l * right_map[l]
    return sim_score
        

#print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))


