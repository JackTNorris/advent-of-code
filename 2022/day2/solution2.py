import numpy as np

def return_array_from_file():
    with open('input.txt') as f:
        lines = f.readlines()        
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n')
        return list(filter(lambda item: len(item) > 0, line_array))
    
def get_rps_value(option):
    if option == "A" or option == "X":
        return 1
    elif option == "B" or option == "Y":
        return 2
    elif option == "C" or option == "Z":
        return 3
    return -1

def i_did_not_lose(my_move, opponent_move):
    # draw handled in main
    if my_move == 1:
        return opponent_move != 2
    elif my_move == 2:
        return opponent_move != 3
    elif my_move == 3:
        return opponent_move != 1
    return False

      

def solution2():
    line_inputs = return_array_from_file()
    score_one = 0
    score_two = 0
    #O(n^2)
    for line in line_inputs:
        opponent_option = line[0]
        second_input = line[2]
        score_one += get_rps_value(second_input)
        #handle tie
        if(get_rps_value(opponent_option) == get_rps_value(second_input)):
            score_one += 3
        #handle win
        elif(i_did_not_lose(get_rps_value(second_input), get_rps_value(opponent_option))):
            score_one += 6
        if second_input == "X":
            if opponent_option == "A":
                score_two += 3
            elif opponent_option == "B":
                score_two += 1
            elif opponent_option == "C":
                score_two += 2
        elif second_input == "Y":
            score_two += get_rps_value(opponent_option) + 3
        elif second_input == "Z":
            if opponent_option == "A":
                score_two += 2
            elif opponent_option == "B":
                score_two += 3
            elif opponent_option == "C":
                score_two += 1
            score_two += 6
        
        
    print("Part 1: " + str(score_one))
    print("Part 2: " + str(score_two))

if __name__ == "__main__":
    solution2()
