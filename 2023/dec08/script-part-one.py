"""
Advent of Code
Day 8 - Part 1 : https://adventofcode.com/2023/day/8
"""

from itertools import cycle
import re


def parse_tree(lines: list[str]):
    """
    Given instructions and a tree description,
    returns the tuple (instructions, tree)
    """
    instructions = lines.pop(0).strip()
    return instructions, { match.group(1).strip(): { "L": match.group(2).strip(), "R": match.group(3).strip()} for line in lines for match in re.finditer(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)', line)}


def binary_search(instructions, tree):
    """
    Given a list of instructions and a tree,
    returns the number of steps to reach 'ZZZ'
    """
    steps = 0
    current_node = "AAA"
    
    while current_node != 'ZZZ':
        current_node = tree[current_node][next(instructions)] # current node is updated to the next node based on the instruction 
        steps += 1

    return steps


def compute_answer(lines: list[str]):
    """
    Given instructions and a tree description,
    returns the answer
    """
    instructions, tree = parse_tree(lines)
    
    instructions = cycle(instructions)

    return binary_search(instructions, tree)


with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))
