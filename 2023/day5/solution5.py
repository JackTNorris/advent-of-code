
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def three_set(arr):
    return [arr[i:i+3] for i in range(0, len(arr), 3)]

def seed_soil_map(seed2soil):
    seed_soil_dict = {}
    for j in range(len(seed2soil)):
        row = seed2soil[j]
        [dest, src, length] = list(map(lambda x: int(x), row.split(' ')))
        for i in range(length):
            print(str(j) + ':' + str(i))
            seed_soil_dict[src+i] = dest+i
    print(seed_soil_dict)

def seed_to_soil(seed_num, seed2soil):
    for j in range(len(seed2soil)):
        row = seed2soil[j]
        [dest, src, length] = list(map(lambda x: int(x), row.split(' ')))
        if seed_num >= src and seed_num <= src + length:
            return seed_num - src + dest
    return seed_num



def part1():
    [seeds, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2location] = list(map(lambda x: x[0] if 'seeds:' in x[0] else x[1:], return_array_from_file('part-1-input.txt')))
    location_nums = []
    seeds = list(map(lambda x: int(x), seeds.split(': ')[1].split(' ')))
    for seed_num in seeds:
        location_nums.append(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_num, seed2soil), soil2fert), fert2water), water2light), light2temp), temp2humid), humid2location))
    print(min(location_nums))
def part2():
    data = return_array_from_file('part-1-input.txt')[0]

if __name__ == "__main__":
    part1()