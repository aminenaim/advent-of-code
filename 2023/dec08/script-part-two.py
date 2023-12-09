"""
Advent of Code
Day 8 - Part 2 : https://adventofcode.com/2023/day/8
"""

from itertools import cycle
from math import lcm
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
    returns the number of steps to reach the first node ending with 'Z' for each node ending with 'A'
    """
    starting_nodes = [node for node in tree.keys() if node.endswith('A')]
    steps = [0] * len(starting_nodes)
    
    for i, node in enumerate(starting_nodes):

        while not node.endswith('Z'):
            node = tree[node][next(instructions)] # current node is updated to the next node based on the instruction 
            steps[i] += 1
        
    return steps


def compute_answer(lines: list[str]):
    """
    Given instructions and a tree description,
    returns the answer
    """
    instructions, tree = parse_tree(lines)

    instructions = cycle(instructions)

    steps = binary_search(instructions, tree)

    # lcm represents the number of steps it takes for all starting 
    # nodes to reach a position ending with 'Z' at the same time.
    return lcm(*steps) 

    
with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))
