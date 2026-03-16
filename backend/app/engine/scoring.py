from collections import Counter

def score(dice_values: list[int]) -> int:
    dice_count = Counter(dice_values) # dice value occurences
    total_score = 0

    # six dice combos
    if (dice_count.total() == 6): # check for 6 dice
        if (len(dice_count) == 6): # straight - each dice value has 1 occurrence 
            return 1500
        elif (len(dice_count.values()) == 3 and all(count == 2 for count in dice_count.values())): # three pairs
            return 1500
        elif (len(dice_count.values()) == 2 and all(count == 3 for count in dice_count.values())): # two triplets
            return 2500
        elif (sorted(dice_count.values()) == [2, 4] and dice_count.total() == 6): # four of a kind and pair
            return 1500

    for face in dice_count:
        # three/four/five of a kind flat values
        if (dice_count[face] == 4):
            total_score += 1000
        elif (dice_count[face] == 5):
            total_score += 2000
        elif (dice_count[face] == 6):
            total_score += 3000
        elif (dice_count[face] >= 3): # dice combos
            if (face == 1):
                total_score += 1000
            else:
                total_score += face * 100 
            
    # single ones
    if (0 < dice_count[1] < 3):
        total_score += dice_count[1] * 100
    
    # single fives
    if (0 < dice_count[5] < 3):
        total_score += dice_count[5] * 50

    return total_score

def is_farkle(dice_values: list[int]) -> bool:
    return score(dice_values) == 0

def is_hot_dice(dice_values: list[int]) -> bool:
    return count_scoring_dice(dice_values) == 6

def count_scoring_dice(dice_values: list[int]) -> int:
    dice_count = Counter(dice_values) # dice value occurences
    num_scoring_dice = 0

    if (dice_count.total() == 6):
        if (len(dice_count) == 6): # straight - each dice value has 1 occurrence 
            return 6
        elif (len(dice_count.values()) == 3 and all(count == 2 for count in dice_count.values())): # three pairs
            return 6
        elif (len(dice_count.values()) == 2 and all(count == 3 for count in dice_count.values())): # two triplets
            return 6
        elif (sorted(dice_count.values()) == [2, 4] and dice_count.total() == 6):
            return 6
    
    for face in dice_count:

        # dice combos
        if (dice_count[face] >= 3):
            num_scoring_dice += dice_count[face]
        elif (face == 1 or face == 5):
            num_scoring_dice += dice_count[face]
        else:
            num_scoring_dice += 0

    return num_scoring_dice
            

