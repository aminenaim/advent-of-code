"""
Advent of Code
Day 13 - Part 2 : https://adventofcode.com/2023/day/13
"""

def parse_grids(lines: str):
    """
    Given lines,
    returns parsed grids
    """
    return [grid.split("\n") for grid in  lines.split("\n\n")]

def rotate90(grid: list[str]):
    return list(zip(*grid))

def find_reflection(grid: list[str]):
    """
    Given a grid, 
    returns the row where a reflection was detected
    """
    for r in range(1, len(grid)):
        upper_subgrid = grid[:r][::-1]
        lower_subgrid = grid[r:]
        
        result = 0

        for row_u, row_l in zip(upper_subgrid, lower_subgrid):
            # for rows in upper and lower subgrids
            for char_u, char_r in zip(row_u, row_l):
                # for chars in upper and lower rows
                if char_u != char_r: # if there is a mismatch, increment the result by 1 
                    result += 1 
        
        if result == 1: # if there is only one smudge in all the grid
            return r
    else:
        return 0

def compute_answer(lines: list[str]):
    """
    Given grids,
    returns the answer
    """
    grids = parse_grids(lines)
    
    return sum([find_reflection(grid) * 100 + find_reflection(rotate90(grid)) for grid in grids])

with open("input.txt", "r") as file:
    lines = file.read()
    print("answer :", compute_answer(lines))

