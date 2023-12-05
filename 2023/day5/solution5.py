
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def two_set(arr):
    return [arr[i:i+2] for i in range(0, len(arr), 2)]

def seed_to_soil(seed_num, seed2soil):
    for j in range(len(seed2soil)):
        row = seed2soil[j]
        [dest, src, length] = list(map(lambda x: int(x), row.split(' ')))
        if seed_num >= src and seed_num <= src + length:
            return seed_num - src + dest
    return seed_num

def loc_to_humid(loc, humid2location):
    for j in range(len(humid2location)):
        row = humid2location[j]
        [dest, src, length] = list(map(lambda x: int(x), row.split(' ')))
        if loc >= dest and loc <= dest + length:
            return loc - dest + src
    return loc

def soil_to_seed_exists(seed_num_inquiry, seeds):
    seeds = two_set(seeds)
    for i in range(len(seeds)):
        [base, length] = seeds[i]
        if seed_num_inquiry >= base and seed_num_inquiry <= base + length:
            return True
    return False



def part1():
    [seeds, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2location] = list(map(lambda x: x[0] if 'seeds:' in x[0] else x[1:], return_array_from_file('part-1-input.txt')))
    location_nums = []
    seeds = list(map(lambda x: int(x), seeds.split(': ')[1].split(' ')))
    for seed_num in seeds:
        location_nums.append(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_to_soil(seed_num, seed2soil), soil2fert), fert2water), water2light), light2temp), temp2humid), humid2location))
    print(min(location_nums))

def part2():
    [seeds, seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2location] = list(map(lambda x: x[0] if 'seeds:' in x[0] else x[1:], return_array_from_file('part-1-input.txt')))
    seeds = list(map(lambda x: int(x), seeds.split(': ')[1].split(' ')))

    location_nums = []
    min_loc = 0
    max_loc = 0
    for i in range(len(humid2location)):
        row = humid2location[i]
        [dest, src, length] = list(map(lambda x: int(x), row.split(' ')))
        min_loc = src if i == 0 else min(min_loc, src)
        max_loc = src if i == 0 else max(max_loc, src)

    for i in range(max_loc):
        print(i)
        seed_inquiry = loc_to_humid(loc_to_humid(loc_to_humid(loc_to_humid(loc_to_humid(loc_to_humid(loc_to_humid(i, humid2location), temp2humid), light2temp), water2light), fert2water), soil2fert), seed2soil)
        
        if soil_to_seed_exists(seed_inquiry, seeds):
            print("FINAL ANSWER: ")
            print(i)
            break

        

if __name__ == "__main__":
    part2()