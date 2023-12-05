
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def extract_winning_mine_array(row):
    nums = row.split(':')[1]
    nums =  list(map(lambda x: list(filter(lambda y: y != '', x.strip().split(' '))), nums.split('|')))
    return nums
    

def part1():
    data = return_array_from_file('part-1-input.txt')[0]
    points = 0
    for row in data:
        row_point = 0
        [win, mine] = extract_winning_mine_array(row)
        for num in mine:
            if num in win:
                row_point = 1 if row_point == 0 else row_point * 2
        points += row_point
    print(points)
          

if __name__ == "__main__":
    part1()