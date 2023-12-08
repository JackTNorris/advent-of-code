import functools

def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
card_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
        'Q': 12, 'K': 13, 'A': 14}

inv_card_map = {v: k for k, v in card_map.items()}

#sort into 5, 4, 3, 2, 1 of kind
#sort music rank, 

def n_of_kind(hand, n):
    hand_set = [0] * 15
    for char in hand:
        hand_set[card_map[char]] = hand_set[card_map[char]] + 1
    return max(hand_set) == n

def has_full_house(hand):
    hand_set = [0] * 15
    for char in hand:
        hand_set[card_map[char]] = (hand_set[card_map[char]] + 1)
    try:
        return bool(hand_set.index(2) and hand_set.index(3))
    except:
        return False

def has_two_pair(hand):
    hand_set = [0] * 15
    for char in hand:
        hand_set[card_map[char]] = hand_set[card_map[char]] + 1
    count2 = 0
    for num in hand_set:
        if num == 2:
            count2 += 1
    return count2 == 2

def get_hand(row):
    return row.split(' ')[0]

def four_of_kind(hand):
    for i in range(len(hand) - 3):
        if hand[i] == hand[i+1] == hand[i+2] == hand[i+3]:
            return True
    return False

def compare_hands(hand1, hand2):
    hand1 = get_hand(hand1)
    hand2 = get_hand(hand2)
    for i in range(len(hand1)):
        if card_map[hand1[i]] > card_map[hand2[i]]:
            return -1
        if card_map[hand1[i]] < card_map[hand2[i]]:
            return 1 
    return 0


def part1():
    five_kind = []
    four_kind = []
    full_house = []
    three_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    data = return_array_from_file('part-2-input.txt')[0]
    for row in data:
        hand = get_hand(row)
        if(n_of_kind(hand, 5)):
            five_kind.append(row)
        elif(n_of_kind(hand, 4)):
            four_kind.append(row);
        elif(has_full_house(hand)):
            full_house.append(row)
        elif(n_of_kind(hand, 3)):
            three_kind.append(row)
        elif(has_two_pair(hand)):
            two_pair.append(row)
        elif(n_of_kind(hand, 2)):
            one_pair.append(row)
        else:
            high_card.append(row)
    five_kind = sorted(five_kind, key = functools.cmp_to_key(compare_hands))
    four_kind = sorted(four_kind, key = functools.cmp_to_key(compare_hands))
    full_house = sorted(full_house, key = functools.cmp_to_key(compare_hands))
    three_kind = sorted(three_kind, key = functools.cmp_to_key(compare_hands))
    two_pair = sorted(two_pair, key = functools.cmp_to_key(compare_hands))
    one_pair = sorted(one_pair, key = functools.cmp_to_key(compare_hands))
    high_card = sorted(high_card, key = functools.cmp_to_key(compare_hands))
    final = five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card
    total = 0
    final.reverse()
    
    for i in range(len(final)):
        print(str(i + 1) + " " + str(final[i]))
        total += (i + 1) * int(final[i].split(' ')[1])
    
    print(total)
    print(has_full_house('77575'))
def part2():
    print('hi')




if __name__ == "__main__":
    part1()




