
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def extract_winning_mine_array(row):
    [cardNum, nums] = row.split(':')
    cardNum = int(cardNum.replace('Card', '').strip())
    nums =  list(map(lambda x: list(filter(lambda y: y != '', x.strip().split(' '))), nums.split('|')))
    return (cardNum, nums)

def part1():
    data = return_array_from_file('part-1-input.txt')[0]
    points = 0
    for row in data:
        row_point = 0
        [cardNum, nums] = extract_winning_mine_array(row)
        [win, mine] = nums
        for num in mine:
            if num in win:
                row_point = 1 if row_point == 0 else row_point * 2
        points += row_point
    print(points)

def part2():
    inventory = [1]*193
    print(inventory)
    data = return_array_from_file('part-2-input.txt')[0]
    for i in range(len(data)):
        row = data[i]
        [cardNum, nums] = extract_winning_mine_array(row)
        [win, mine] = nums
        num_match = 0
        for num in mine:
            if num in win:
                num_match += 1
        
        for j in range(num_match):
            k = i + j + 1
            for z in range(inventory[i]):
                inventory[k] = inventory[k] + 1
    print(sum(inventory)) 

if __name__ == "__main__":
    part2()