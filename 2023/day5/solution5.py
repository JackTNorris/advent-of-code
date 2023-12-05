
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def part1():
    data = return_array_from_file('part-1-input.txt')[0]


def part2():
    data = return_array_from_file('part-1-input.txt')[0]

if __name__ == "__main__":
    part2()