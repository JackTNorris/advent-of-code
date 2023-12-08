import functools

def return_array_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        line_string = ""
        for line in lines:
            line_string += line
        line_array = line_string.split('\n\n')
        return list(map(lambda item_set: item_set.split('\n'), line_array))

card_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 0,
        'Q': 12, 'K': 13, 'A': 14}

j_card_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 0,
        'Q': 12, 'K': 13, 'A': 14}

hands = {'five_kind': 0, 'four_kind': 1, 'full_house': 2, 'three_kind': 3, 'two_pair': 4, 'one_pair': 5, 'high_card': 6}

inv_card_map = {v: k for k, v in card_map.items()}

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
        print(final[i])
        total += (i + 1) * int(final[i].split(' ')[1])
    print(total)

def convert_ideal(my_hand):
    my_best_hand = ""
    best_hand_val = 6
    for char in card_map.keys():
        best_hand = my_hand.replace('J', char)
        prev_best_hand_val = best_hand_val
        if(n_of_kind(best_hand, 5)):
            best_hand_val = min(best_hand_val, hands['five_kind'])
        elif(n_of_kind(best_hand, 4)):
            best_hand_val = min(best_hand_val, hands['four_kind'])
        elif(has_full_house(best_hand)):
            best_hand_val = min(best_hand_val, hands['full_house'])
        elif(n_of_kind(best_hand, 3)):
            best_hand_val = min(best_hand_val, hands['three_kind'])
        elif(has_two_pair(best_hand)):
            best_hand_val = min(best_hand_val, hands['two_pair'])
        elif(n_of_kind(best_hand, 2)):
            best_hand_val = min(best_hand_val, hands['one_pair'])
        else:
            best_hand_val = min(best_hand_val, hands['high_card'])
        if(best_hand_val < prev_best_hand_val):
            my_best_hand = best_hand
        if my_best_hand == "":
            my_best_hand = my_hand
    return my_best_hand
 

def compare_hands_jack(hand1, hand2):
    hand1 = (get_hand(hand1))
    hand2 = (get_hand(hand2))
    for i in range(len(hand1)):
        if j_card_map[hand1[i]] > j_card_map[hand2[i]]:
            return -1
        if j_card_map[hand1[i]] < j_card_map[hand2[i]]:
            return 1 
    return 0    

def part2():
    five_kind = []
    four_kind = []
    full_house = []
    three_kind = []
    two_pair = []
    one_pair = []
    high_card = []
    data = return_array_from_file('part-2-input.txt')[0]
    for row in data:
        hand = convert_ideal(get_hand(row))
        if(n_of_kind(hand, 5)):
            five_kind.append(row)
        elif(n_of_kind(hand, 4)):
            four_kind.append(row)
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
    five_kind = sorted(five_kind, key = functools.cmp_to_key(compare_hands_jack))
    four_kind = sorted(four_kind, key = functools.cmp_to_key(compare_hands_jack))
    full_house = sorted(full_house, key = functools.cmp_to_key(compare_hands_jack))
    three_kind = sorted(three_kind, key = functools.cmp_to_key(compare_hands_jack))
    two_pair = sorted(two_pair, key = functools.cmp_to_key(compare_hands_jack))
    one_pair = sorted(one_pair, key = functools.cmp_to_key(compare_hands_jack))
    high_card = sorted(high_card, key = functools.cmp_to_key(compare_hands_jack))
    final = five_kind + four_kind + full_house + three_kind + two_pair + one_pair + high_card
    total = 0
    final.reverse()
    for i in range(len(final)):
        total += (i + 1) * int(final[i].split(' ')[1])
    print(total)




if __name__ == "__main__":
    part1()
    part2()




