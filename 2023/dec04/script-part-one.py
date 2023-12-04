"""
Advent of Code
Day 4 - Part 1 : https://adventofcode.com/2023/day/4
"""

import math

def parse_card(card: str):
    """
    Given a card string,
    returns a tuple (winning_numbers, card_numbers)
    """
    return [numbers.split() for numbers in card.split(":")[1].split("|")]

def compute_sum(lines: list[str]):
    """
    Given a list of cards (strings),
    returns the the sum of the worths of each cards
    """
    cards = [parse_card(line) for line in lines]

    result = 0

    for winning_numbers, numbers in cards:
        points = [number for number in numbers if number in winning_numbers]
        result += math.floor(2 ** (len(points) - 1))
    
    return result


with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_sum(lines))

