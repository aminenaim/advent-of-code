"""
Advent of Code
Day 7 - Part 1 : https://adventofcode.com/2023/day/7
"""

from collections import Counter

STRENGTHS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def parse_hands(lines: str):
    """
    Given a list of hands (list of strings),
    returns a list of tuples (cards, bid)
    """
    return [(item[0], int(item[1])) for item in (line.split() for line in lines)]

def compute_strength(hand):
    """
    Given a hand,
    returns its strength
    """
    frequencies = Counter([STRENGTHS.index(card) for card in hand]).values()

    frequencies = sorted(frequencies)

    kinds = [
        ([1, 1, 1, 1, 1], 1),   # high card
        ([1, 1, 1, 2], 2),      # one pair
        ([1, 2, 2], 3),         # two pairs
        ([1, 1, 3], 4),         # three of a kind
        ([2, 3], 5),            # full house
        ([1, 4], 6),            # four of a kind
        ([5], 7),               # five of a kind
    ]

    for kind, strength in kinds:
        if frequencies == kind:
            return [strength] + [STRENGTHS.index(c) for c in hand]
    else:
        return [0]

def compute_answer(lines: list[str]):
    """
    Given a list of tuples (hand, bid),
    returns the sum of all the bids*rank factors
    """
    hands = parse_hands(lines)
    
    hands_strengths = [(compute_strength(hand), bid) for hand, bid in hands]
    
    sorted_hands = sorted(hands_strengths, key=lambda h: h[0])
    
    return sum([index*bid for index, (_, bid) in enumerate(sorted_hands, 1)])

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))
