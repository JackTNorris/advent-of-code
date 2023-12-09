import functools

def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def calc_diff_array(nums, diff_list):
    diffs = []
    for i in range(1, len(nums)):
        diffs.append(nums[i] - nums[i-1])
    diff_list.append(diffs)
    temp_diff = map(lambda y: abs(y), diffs)
    if max(temp_diff) != 0:
        calc_diff_array(diffs, diff_list)
    return diff_list

def calc_final_num(diff_list, part_two = False):
    diff_list.reverse()
    final_nums = [0]
    for i in range(1, len(diff_list)):
        if part_two:
            final_nums.append(diff_list[i][0] - final_nums[i - 1])
        else:
            final_nums.append(diff_list[i][-1:][0] + final_nums[i - 1])
    return final_nums[-1:][0]


def part1():
    data = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), return_array_from_file('part-2-input.txt')[0]))
    sum = 0
    for nums in data:
        sum+=calc_final_num(calc_diff_array(nums, [nums]))
    print(sum)

def part2():
    data = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), return_array_from_file('part-2-input.txt')[0]))
    sum = 0
    for nums in data:
        sum+=calc_final_num(calc_diff_array(nums, [nums]), True)
    print(sum)

if __name__ == "__main__":
    part2()
