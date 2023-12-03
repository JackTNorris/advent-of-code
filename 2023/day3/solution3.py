
def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))


def checkAdjacent(number_indexes_list, symbol_indexes):
    for number_index in number_indexes_list:
        if number_index in symbol_indexes or number_index + 1 in symbol_indexes or number_index - 1 in symbol_indexes:
            return True
    return False

def numberIndexesLists(row):
    number_indexes_lists = []
    number_indexes = []
    for i in range(len(row)):
        if row[i] >= '0' and row[i] <= '9':
            number_indexes.append(i)
        else:
            if len(number_indexes) > 0:
                number_indexes_lists.append(number_indexes)
                number_indexes = []
        if i == len(row) - 1:
            number_indexes_lists.append(number_indexes)
            number_indexes = []

    return number_indexes_lists;

def symbolIndexes(row):
    symbol_indexes = []
    for i in range(len(row)):
        char = row[i]
        if char != '.' and not(char >= '0' and char <= '9'):
            symbol_indexes.append(i)
    return symbol_indexes

def extractNumber(number_indexes, row):
    return int(''.join(row[number_indexes[0]:(number_indexes[-1:][0] + 1)]))

def part1():
    data = return_array_from_file('part-1-input.txt')[0]
    sum = 0
    for i in range(len(data)):
        row = data[i]
        number_indexes_lists = numberIndexesLists(row)
        symbol_indexes = symbolIndexes(row)
        for number_indexes_list in number_indexes_lists:
            if checkAdjacent(number_indexes_list, symbol_indexes):
                sum+=extractNumber(number_indexes_list, row)
            elif i != 0 and checkAdjacent(number_indexes_list, symbolIndexes(data[i-1])):
                sum+=extractNumber(number_indexes_list, row)
            elif i != len(data)-1 and checkAdjacent(number_indexes_list, symbolIndexes(data[i+1])):
                sum+=extractNumber(number_indexes_list, row)
    print(sum)

    




def part2():
    print()

          

if __name__ == "__main__":
    part1()