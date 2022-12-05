def return_array_from_file():
    with open('input.txt') as f:
        return list(map(lambda line:  line.replace('\n', ''),f.readlines())) 

def array_contains_value(value, array):
    return len(list(filter(lambda item: item == value, array))) > 0

def array1_contains_array2(array1, array2):
    for i in range(len(array2)):
        if not array_contains_value(array2[i], array1):
            return False
    return True

def array1_contains_any_array2(array1, array2):
    for i in range(len(array2)):
        if array_contains_value(array2[i], array1):
            return True
    return False


def solution4():
    input = return_array_from_file()
    contained_range_count = 0
    contained_any_range_count = 0
    for line in input:
        range_one_bounds, range_two_bounds = line.split(',')
        range_one_bounds = range_one_bounds.split('-')
        range_two_bounds = range_two_bounds.split('-')
        
        set_one = []
        set_two = []
        for i in range(int(range_one_bounds[0]), int(range_one_bounds[1]) + 1):
            set_one.append(i)
        for i in range(int(range_two_bounds[0]), int(range_two_bounds[1]) + 1):
            set_two.append(i)
        if array1_contains_array2(set_one, set_two) or array1_contains_array2(set_two, set_one):
            contained_range_count += 1
        if array1_contains_any_array2(set_one, set_two) or array1_contains_any_array2(set_two, set_one):
            contained_any_range_count += 1

    print("Part 1: " + str(contained_range_count)) 
    print("Part 2: " + str(contained_any_range_count)) 
        

if __name__ == "__main__":
    solution4()
