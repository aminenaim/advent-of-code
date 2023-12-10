"""
Advent of Code
Day 10 - Part 1 : https://adventofcode.com/2023/day/10
"""
import os

def parse_pipes(lines: list[str]):
    """
    Given a list of pipes (strings),
    returns the pipes matrix
    """
    return [line.strip() for line in lines]


def navigate(grid: list[list[str]]):
    """
    Given a grid, finds the starting cordinates and
    returns the steps number to get to the farthest tile from the starting tile
    """
    seen = []
    s = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == 'S'][0]
    current = s
    

    while current != s or len(seen) == 0:
        row, col = current
        char = grid[row][col]
            
        # upward motion
        if row > 0 and char in "|SJL" and grid[row-1][col] in "|F7" and (row-1, col) not in seen:
            seen.append((row-1, col))
            current = (row-1, col)
            continue;
        
        # downward motion
        if row < len(grid)-1 and char in "|SF7" and grid[row+1][col] in "|JL" and (row+1, col) not in seen:
            seen.append((row+1, col))
            current = (row+1, col)
            continue;
        
        # left motion
        if col > 0 and char in "S-J7" and grid[row][col-1] in "-LF" and (row, col-1) not in seen:
            seen.append((row, col-1))
            current = (row, col-1)
            continue;
        
        # right motion
        if col < len(grid)-1 and char in "S-LF" and grid[row][col+1] in "-J7" and (row, col+1) not in seen:
            seen.append((row, col+1))
            current = (row, col+1)
            continue;

        break;
    
    return (len(seen)+1) // 2

def compute_answer(lines: list[str]):
    """
    Given a list of pipes,
    returns the number of steps to 
    """
    grid = parse_pipes(lines)

    return navigate(grid)

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))

