"""
Advent of Code
Day 2 - Part 1 : https://adventofcode.com/2023/day/2
--
Here is a more "compact" version. I tend to prefer codes with more functions to split into logical steps.
This version uses regular expressions and tuples for a cleaner and more concise implementation.
"""

import re

def parse_game(game: str):
    """
    Given a game string,
    returns a list of tuples containing amount and color information
    """
    return re.findall(r"(\d+) (red|green|blue)", game.split(":")[1])

def compute_sum(games: list[str]):
    """
    Given a list of games (strings),
    returns the sum of the powers of each set of cubes
    """
    lines = [parse_game(game) for game in games]

    result = 0

    for index, line in enumerate(lines):
        bag = {"red": 12, "green": 13, "blue": 14}
        result += index+1 if all(int(amount) <= bag[color] for amount, color in line) else 0

    return result

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_sum(lines))
