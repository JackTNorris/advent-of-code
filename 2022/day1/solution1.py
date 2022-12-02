import numpy as np

def return_array_from_file():
    with open('input.txt') as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

def solution1():
    elf_inventories = return_array_from_file()
    elf_calories = []

    for i in range(0, len(elf_inventories)):
        elf_calories.append(sum(map(lambda s: int(s),elf_inventories[i])))
    top_cal = max(elf_calories)
    print("Part 1: " + str(top_cal))
    elf_calories.remove(top_cal)
    sec_cal = max(elf_calories)
    elf_calories.remove(sec_cal)
    thr_cal = max(elf_calories)
    print("Part 2: " + str(top_cal + sec_cal + thr_cal))


if __name__ == "__main__":
    solution1()
