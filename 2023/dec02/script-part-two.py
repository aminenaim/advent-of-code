"""
Advent of Code
Day 2 - Part 2 : https://adventofcode.com/2023/day/2
"""

COLORS = ["red", "green", "blue"]

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

def parse_game(line: str):
    """
    Given a line, returns a tuple (game_number, color_sets) with color_sets being a list of dictionaries of parsed colors
    """
    game_number = int(line.split(":")[0].split()[1])
    color_sets = [parse_color_set(color_set.split(",")) for color_set in line.split(":")[1].split(";")]

    return game_number, color_sets

def compute_fewer_number(color_sets):
    """
    Given a list of color sets,
    returns the fewer amounts of cubes for each color
    """
    max_cubes = {color: max(cubes[color] for cubes in color_sets) for color in COLORS}
    
    return max_cubes["red"], max_cubes["green"], max_cubes["blue"]

answer = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        game_number, color_sets = parse_game(line)
        red, green, blue = compute_fewer_number(color_sets)
        answer += red * green * blue

print("answer :", answer)