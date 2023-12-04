"""
Advent of Code
Day 4 - Part 2 : https://adventofcode.com/2023/day/4
"""

def parse_card(card: str):
    """
    Given a card string,
    returns a tuple (winning_numbers, card_numbers)
    """
    return [numbers.split() for numbers in card.split(":")[1].split("|")]

def compute_sum(lines: list[str]):
    """
    Given a list of cards (strings),
    returns the number of scratchcards
    """
    cards = [parse_card(line) for line in lines]

    points = []
    for winning_number, numbers in cards:
        points.append(len([number for number in numbers if number in winning_number]))

    copies = [1] * len(points)

    for i, point in enumerate(points):
        for j in range(point):
            copies[i + j + 1] += copies[i]

    return sum(copies)

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_sum(lines))

