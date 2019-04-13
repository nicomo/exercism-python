from collections import Counter
from functools import partial

# Score categories
# Change the values as you see fit
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


# only one number in the set
def yacht(dice):
    return 50 if len(set(dice)) == 1 else 0

# cases ONES to SIXES
def sum_numbers(number, dice):
    return sum(num for num in dice if num == number)

# full house, i.e. 3 of a kind + 2 of a kind
def full_house(dice):
    counter = Counter(dice)
    if set(counter.values()) == {3, 2}:
        return sum(dice) 
    else:
        return 0

def four_of_a_kind(dice):
    counter = Counter(dice)
    num, c = counter.most_common()[0]
    if c >= 4:
        return 4 * num
    else:
        return 0

# 1, 2, 3, 4, 5
def little_straight(dice):
    if set(dice) == {1, 2, 3, 4, 5}:
        return 30
    else:
        return 0

# 2, 3, 4, 5, 6
def big_straight(dice):
    if set(dice) == {2, 3, 4, 5, 6}:
        return 30
    else:
        return 0

def choice(dice):
    return sum(dice)

def score(dice, category):
    return funcs[category](dice)

funcs = [
    yacht,
    partial(sum_numbers, 1),
    partial(sum_numbers, 2),
    partial(sum_numbers, 3),
    partial(sum_numbers, 4),
    partial(sum_numbers, 5),
    partial(sum_numbers, 6),
    full_house,
    four_of_a_kind,
    little_straight,
    big_straight,
    choice,
]