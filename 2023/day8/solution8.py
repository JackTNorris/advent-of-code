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

def lcm(nums):
    found = False
    max_num = max(nums)
    i = 2
    while not found:
        temp_found = True
        for n in nums:
            if max_num * i % n != 0:
                temp_found = False
                i += 1
                break
        found = temp_found
    return i * max_num

def part2():
    steps = []
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

    for current in currents:
        local_step = 0
        while current[-1:] != 'Z':
            rl = instructions[local_step % len(instructions)]
            current = node_map[current][0 if rl == 'L' else 1]
            local_step += 1
        steps.append(local_step)
        total = 1
        for step in steps:
            total *= step
    print(steps)
    from math import gcd
    lcm = 1
    for i in steps:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)

if __name__ == "__main__":
    part2()



20685524831999
