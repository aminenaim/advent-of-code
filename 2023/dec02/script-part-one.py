"""
Advent of Code
Day 2 - Part 1 : https://adventofcode.com/2023/day/2
"""

COLORS = ["red", "green", "blue"]
REDS = 12
GREENS = 13
BLUES = 14

def parse_color_set(color_set: list):
    """
    Given a list of strings of the format ["1 red", "2 green", "3 blue", "4 red"...],
    returns a dictionary containing the amount of occurrence for each color
    """
    colors = {color: 0 for color in COLORS}

    for set in color_set:
        amount, color = map(str.strip, set.split())
        colors[color] += int(amount)

    return colors

def parse_games(line: str):
    """
    Given a line, returns a tuple (game_number, color_sets) with color_sets being a list of dictionaries of parsed colors
    """
    game_number = int(line.split(":")[0].split()[1])
    color_sets = [parse_color_set(color_set.split(",")) for color_set in line.split(":")[1].split(";")]

    return game_number, color_sets

def has_matching_amounts(color_sets):
    """
    Given a dictionary of color sets,
    returns True if amounts match predefined amounts
    """
    return REDS >= color_sets["red"] and GREENS >= color_sets["green"] and BLUES >= color_sets["blue"]

game_ids_sum = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        game_number, color_sets = parse_games(line)
        matches = all(has_matching_amounts(color_set) for color_set in color_sets)

        if matches:
            game_ids_sum += game_number

print("answer :", game_ids_sum)
