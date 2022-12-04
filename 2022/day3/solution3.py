def return_array_from_file():
    with open('input.txt') as f:
        return list(map(lambda line:  line.replace('\n', ''),f.readlines())) 

def letter_value(letter):
    if letter.lower() == letter:
        return ord(letter) - 96
    else:
        return ord(letter) - 38
    

def solution3():
    #part 1
    input = return_array_from_file()
    score = 0
    for line in input:
        rucksack_one = line[:int(len(line)/2)]
        rucksack_two = line[int(len(line)/2):]
        finished = False
        for letter in rucksack_one:
            if rucksack_two.find(letter) > -1 and not finished:
                score += letter_value(letter)
                finished = True
                
    print("Part 1: " + str(score))

    #part 2
    score = 0
    for i in range(int(len(input)/3)):
        print(i)
        rucksack_one = input[i*3]
        rucksack_two = input[i*3 + 1]
        rucksack_three = input[i*3 + 2]
        finished = False
        for letter in rucksack_one:
            if rucksack_two.find(letter) > -1 and not finished and rucksack_three.find(letter) > -1:
                score += letter_value(letter)
                finished = True
    print("Part 2: " + str(score))



if __name__ == "__main__":
    solution3()
