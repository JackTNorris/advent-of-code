
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def num_win_ways(time, distance):
    num_win = 0
    for ms in range(1, time):
        temp_dist = (time - ms) * ms
        #this is dumb, should technically be finished at equal to
        if temp_dist > distance:
            num_win+=1
    return num_win

def part1():
    [times, distances] = list(map(lambda x:  list(filter(lambda y: y != '', x.split(':')[1].strip().split(' '))), return_array_from_file('part-2-input.txt')[0]))
    times = list(map(lambda x: int(x), times))
    distances = list(map(lambda x: int(x), distances))
    win_prod = 1

    for i in range(len(times)):
        nw = num_win_ways(times[i], distances[i])
        win_prod *= 1 if nw == 0 else nw
    print(win_prod)

def part2():
    [times, distances] = list(map(lambda x:  int(x.split(':')[1].replace(' ', '')), return_array_from_file('part-2-input.txt')[0]))
    i = 0
    for ms in range(times):
        temp_dist = (times - ms) * ms
        #this is dumb, should technically be finished at equal to
        if temp_dist > distances:
            i = ms
            break
    print(times - 2*i + 1)



if __name__ == "__main__":
    part2()