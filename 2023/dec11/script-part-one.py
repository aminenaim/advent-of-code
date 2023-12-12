"""
Advent of Code
Day 11 - Part 1 : https://adventofcode.com/2023/day/11
"""

def parse_image(lines: list[str]):
    """
    Given an image of space (list of strings),
    returns the space grid
    """
    return [line.strip() for line in lines]

def compute_distance(grid: list[str]):
    """
    Given a grid, finds all the empty rows and columns,
    returns the sum of the shortest lengths between every pair of galaxies
    """
    # finding every empty rows and columns
    empty_rows = [r for r, row in enumerate(grid) if all(char == '.' for char in row)]
    empty_cols = [c for c, col in enumerate(zip(*grid)) if all(char == '.' for char in col)]

    galaxies = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == '#']

    distance = 0

    distance = 0
    expansion_factor = 2

    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:
            # compute the distance between two points
            for r in range(min(r1, r2), max(r1, r2)):
                distance += expansion_factor if r in empty_rows else 1 
            for c in range(min(c1, c2), max(c1, c2)):
                distance += expansion_factor if c in empty_cols else 1

    return distance


def compute_answer(lines: list[str]):
    """
    Given an "image" of space,
    returns the answer
    """
    grid = parse_image(lines)
    return compute_distance(grid)


with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))

