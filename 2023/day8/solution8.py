import functools

def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def part1():
    steps = 0
    [instructions, nodes] = return_array_from_file('part-2-input.txt')
    instructions = instructions[0]
    node_map = {}
    for node in nodes:
        [key, values] = node.split('=')
        key = key.strip()
        values = list(map(lambda x: x.strip(), values.strip().strip('(').strip(')').split(',')))
        node_map[key] = values
    current = 'AAA'
    while current != 'ZZZ':
        rl = instructions[steps % len(instructions)]
        current = node_map[current][0 if rl == 'L' else 1]
        steps += 1

    print(steps)

def part2():
    steps = 0
    [instructions, nodes] = return_array_from_file('part-2-input.txt')
    instructions = instructions[0]
    node_map = {}
    for node in nodes:
        [key, values] = node.split('=')
        key = key.strip()
        values = list(map(lambda x: x.strip(), values.strip().strip('(').strip(')').split(',')))
        node_map[key] = values
    
    def has_nodes_not_end_z(c):
        for g in c:
            if g[-1:] != 'Z':
                return True

    currents = list(filter(lambda x: x[-1:] == 'A', node_map.keys()))
    while (has_nodes_not_end_z(currents)):
        rl = instructions[steps % len(instructions)]
        for c in range(len(currents)):
            currents[c] = node_map[currents[c]][0 if rl == 'L' else 1]
        steps += 1
    print(steps)
if __name__ == "__main__":
    part2()




