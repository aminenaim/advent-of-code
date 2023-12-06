"""
Advent of Code
Day 6 - Part 2 : https://adventofcode.com/2023/day/6
--
Basically today's challenge is solving a quadratic equation.
Never thought I would use this again since high school.
Here we have something along : x² - x*time + distance = 0 with x being the duration we pressed the button.
"""

from math import ceil, floor, sqrt


def parse_document(lines: str):
    """
    Given a document (list of strings),
    returns a tuple (time, distance)
    """
    # fixing the kerning by ignoring the spaces between the numbers on each line
    return [int(line.split(":")[1].replace(" ", "")) for line in lines]

def compute_answer(lines: list[str]):
    """
    Given a tuple of ints (time, distance),
    returns the factor between every number of ways to beat the time-distance record
    """
    time, distance = parse_document(lines)

    # we compute b_one and b_two our two real solutions
    new_distance = distance + 1
    b_one = (time + sqrt(time**2-4*new_distance)) / 2
    b_two = (time - sqrt(time**2-4*new_distance)) / 2

    # the number of ways is the number of int solutions between b_one and b_two
    # we floor the top value and ceil the bottom value then add 1 to include the first value
    ways = floor(b_one) - ceil(b_two) + 1
    
    return ways

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))

