import sys, os
import re
sys.path.append('../../')
import aoc_utils


def part1():
    data = "".join(aoc_utils.return_array_from_file('input.txt')[0])
    mult = re.search("mul\([0-9]+,[0-9]+\)", data) #sufficient for now
    res = 0
    while mult != None:
        temp = re.findall("[0-9]+",data[mult.span()[0]:mult.span()[1]])
        res += int(temp[0]) * int(temp[1])
        data = data[mult.span()[1]:]
        mult = re.search("mul\([0-9]+,[0-9]+\)", data) #sufficient for now
    return res
    


def part2():
    data = "".join(aoc_utils.return_array_from_file('input.txt')[0])
    mult = re.search("mul\([0-9]+,[0-9]+\)", data) #sufficient for now
    do_it = True
    res = 0
    while mult != None:
        
        do_dont = list(map(lambda x: x[::-1], re.findall("\)\(t'nod|\)\(od", data[0:mult.span()[0]][::-1]))) #reversing string to get last occurence of do or don't up to mult op
        if len(do_dont) > 0:
            if do_dont[0] == "don't()":
                do_it = False
            else:
                do_it = True
        
        temp = re.findall("[0-9]+",data[mult.span()[0]:mult.span()[1]])
        res += int(temp[0]) * int(temp[1]) if do_it else 0
        data = data[mult.span()[1]:]
        mult = re.search("mul\([0-9]+,[0-9]+\)", data) #sufficient for now
    return res

print('Part 1: ', part1())
print('Part 2: ', part2())
            



        
        