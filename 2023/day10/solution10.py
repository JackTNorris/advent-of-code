import functools

def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
|_
J is a 90-degree bend connecting north and west.
_|
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

"""

horizontal_components = '-LJ'

#[row, column]
def move(pipe_char, curr_pos, prev_pos):
    if pipe_char == '|':
        #next row, don't go to same spot as before
        return [curr_pos[0] + 1, curr_pos[1]] if prev_pos[0] != curr_pos[0] + 1 else [curr_pos[0] - 1, curr_pos[1]]
    elif pipe_char == '-':
        #new col, don't go to same col as before
        return [curr_pos[0], curr_pos[1] + 1] if prev_pos[1] != curr_pos[1] + 1 else [curr_pos[0], curr_pos[1] - 1]
    elif pipe_char == 'L':
        #new col or new row, just don't be in same spot as before
        #if same row as previous move
        if curr_pos[0] == prev_pos[0]:
            #move to next row (above)
            return [curr_pos[0] - 1, curr_pos[1]]
        #if same col as previous move
        elif curr_pos[1] == prev_pos[1]:
            #move to next column (right)
            return [curr_pos[0], curr_pos[1] + 1]
    elif pipe_char == 'J':
        #new col or new row, just don't be in same spot as before
        #if same row as previous move
        if curr_pos[0] == prev_pos[0]:
            #move to next row (below)
            return [curr_pos[0] - 1, curr_pos[1]]
        #if same col as previous move
        elif curr_pos[1] == prev_pos[1]:
            #move to next column (left)
            return [curr_pos[0], curr_pos[1] - 1]
    elif pipe_char == '7':
        #new col or new row, just don't be in same spot as before
        #if same row as previous move
        if curr_pos[0] == prev_pos[0]:
            #move to next row (below)
            return [curr_pos[0] + 1, curr_pos[1]]
        #if same col as previous move
        elif curr_pos[1] == prev_pos[1]:
            #move to next column (left)
            return [curr_pos[0], curr_pos[1] - 1]
    elif pipe_char == 'F':
        #new col or new row, just don't be in same spot as before
        #if same row as previous move
        if curr_pos[0] == prev_pos[0]:
            #move to next row (below)
            return [curr_pos[0] + 1, curr_pos[1]]
        #if same col as previous move
        elif curr_pos[1] == prev_pos[1]:
            #move to next column (left)
            return [curr_pos[0], curr_pos[1] + 1]
    else:
        return curr_pos

def traverse_loop(start_spot, pipe_map):
    count = 1
    new_spot = list([start_spot[0] + 1, start_spot[1]])
    char = pipe_map[new_spot[0]][new_spot[1]]
    while char != 'S':
        print(char)
        temp_start_spot = list(new_spot)
        count += 1
        new_spot = move(pipe_map[new_spot[0]][new_spot[1]], new_spot, start_spot)
        print("new spot: ")
        print(new_spot)
        char = pipe_map[new_spot[0]][new_spot[1]]
        start_spot = temp_start_spot
    print(count)

def part1():
    data = return_array_from_file('part-2-input.txt')[0]
    pipe_map = []
    start = [] #top left of input
    for i in range(len(data)):
        pipe_map.append(list(data[i]))
        if data[i].find('S') >= 0:
            start.append(i)
            start.append(data[i].find('S'))
    print(pipe_map)
    print(start)
    traverse_loop(start, pipe_map)

def part2():
    print('hi')

if __name__ == "__main__":
    part1()
