
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))
    


def isNumeric(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def part1():
    r = 12
    g = 13
    b = 14
    blue = 'blue'
    red = 'red'
    green = 'green'
    data = return_array_from_file('part-1-input.txt')[0]
    total_won = 0
    for row in data:
        valid = True
        [game, hands] = row.split(':')
        game = int(game.split(' ')[1])
        hands = hands.split(';')
        for hand in hands:
            draws = list(map(lambda x: x.strip(), hand.split(',')))
            for draw in draws:
                if red in draw:
                    if(int(draw.split(' ')[0]) > r):
                        valid = False
                if blue in draw:
                    if(int(draw.split(' ')[0]) > b):
                        valid = False
                if green in draw:
                    if(int(draw.split(' ')[0]) > g):
                        valid = False
        if valid:
            total_won += game   
    print(total_won)


def part2():
    blue = 'blue'
    red = 'red'
    green = 'green'
    data = return_array_from_file('part-1-input.txt')[0]
    power_sum = 0
    for row in data:
        min_r = 0
        min_g = 0
        min_b = 0
        valid = True
        [game, hands] = row.split(':')
        game = int(game.split(' ')[1])
        hands = hands.split(';')
        for hand in hands:
            draws = list(map(lambda x: x.strip(), hand.split(',')))
            for draw in draws:
                if red in draw:
                    min_r = max(int(draw.split(' ')[0]), min_r)
                if blue in draw:
                    min_b = max(int(draw.split(' ')[0]), min_b)
                if green in draw:
                    min_g = max(int(draw.split(' ')[0]), min_g)
        power_sum += min_r * min_g * min_b
    print(power_sum)

          

if __name__ == "__main__":
    part2()