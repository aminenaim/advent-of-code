"""
Advent of Code
Day 13 - Part 1 : https://adventofcode.com/2023/day/13
"""

def parse_grids(lines: str):
    """
    Given lines,
    returns parsed grids
    """
    return [grid.split("\n") for grid in  lines.split("\n\n")]


def find_reflection(grid: list[str]):
    """
    Given a grid, 
    returns the row where a reflection was detected
    """
    for r in range(1, len(grid)):
        upper_subgrid = grid[:r][::-1]
        lower_subgrid = grid[r:]

        # truncates upper and lower subgrids to the minimal size
        upper_subgrid, lower_subgrid = upper_subgrid[:len(lower_subgrid)], lower_subgrid[:len(upper_subgrid)]

        if upper_subgrid == lower_subgrid:
            return r
    else:
        return 0

def compute_answer(lines: list[str]):
    """
    Given grids,
    returns the answer
    """
    grids = parse_grids(lines)
    
    return sum([find_reflection(grid) * 100 + find_reflection(list(zip(*grid))) for grid in grids])

with open("input.txt", "r") as file:
    lines = file.read()
    print("answer :", compute_answer(lines))

