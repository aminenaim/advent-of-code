"""
Advent of Code
Day 2 - Part 2 : https://adventofcode.com/2023/day/2
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

def compute_power_sum(games: list[str]):
    """
    Given a list of games (strings),
    returns the sum of the powers of each set of cubes
    """
    lines = [parse_game(game) for game in games]

    result = 0

    for line in lines:
        fewers = {"red": 0, "green": 0, "blue": 0}

        for amount, color in line:
            fewers[color] = max(fewers[color], int(amount))

        result += fewers["red"] * fewers["green"] * fewers["blue"]

    return result

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_power_sum(lines))
