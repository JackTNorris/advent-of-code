
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
    data = return_array_from_file('part-1-input.txt')[0]
    sum = 0
    for row in data:
        num1 = ''
        num2 = ''
        rev_row = row[::-1]
        for i in range(0, len(row)):
            if isNumeric(row[i]) and len(num1) == 0:
                num1 = row[i]
            if isNumeric(rev_row[i]) and len(num2) == 0:
                num2 = rev_row[i]
        try:
            print(row + ": " + str(int(num1 + num2)))
            sum += int(num1 + num2)
        except ValueError:
            pass
    print(sum)


def part2():
    dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    data = return_array_from_file('part-2-input.txt')[0]
    sum = 0
    for row in data:
        num1 = ''
        num2 = ''
        indexFirstNumeric = -1
        indexLastNumeric = -1
        rev_row = row[::-1]
        for i in range(0, len(row)):
            if isNumeric(row[i]) and indexFirstNumeric < 0:
                indexFirstNumeric = i
                num1 = row[i]
            if isNumeric(rev_row[i]) and indexLastNumeric < 0:
                indexLastNumeric = len(row) - i - 1
                num2 = rev_row[i]

        for key in dict.keys():
            try:
                if row.index(key) < indexFirstNumeric:
                    indexFirstNumeric = row.index(key)
                    num1 = dict[key]
            except ValueError:
                pass
            try:
                if row.rindex(key) > indexLastNumeric:
                    indexLastNumeric = row.rindex(key)
                    num2 = dict[key]
            except ValueError:
                pass
        try:
            print(row + ": " + str(int(num1 + num2)))
            sum += int(num1 + num2)
        except ValueError:
            pass
    print(sum)

          

if __name__ == "__main__":
    part2()