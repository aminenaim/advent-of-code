"""
Advent of Code
Day 3 - Part 2 : https://adventofcode.com/2023/day/3
"""

import re

def lookup_gears(lines: list[str]):
    """
    Given a matrix,
    returns a list of tuples containing coordinates of gears
    """
    gears = []
    for x, line in enumerate(lines):
        for match in re.finditer(r"(\*)", line.strip()):
            gears.append((x, match.start()))
        
    return gears

def cell_neighbors(x, y, matrix_length):
    """
    Given x, y coordinates returns a list of neighboring cells within the matrix bounds
    """
    neighbors = []
    # define the relative coordinates of neighboring cells
    relative_coordinates = [(-1, -1), (-1, 0), (-1, 1),
                            (0, -1),           (0, 1),
                            (1, -1),  (1, 0),  (1, 1)]

    for dx, dy in relative_coordinates:
        new_x, new_y = x + dx, y + dy

        # check if the new coordinates are within the matrix bounds
        if 0 <= new_x < matrix_length and 0 <= new_y < matrix_length:
            neighbors.append((new_x, new_y))

    return neighbors

def compute_sum(lines: list[str]):
    """
    Given a schematic (list of strings),
    returns the sum of the gear ratios
    """
    part_sum = 0
    gears = lookup_gears(lines)

    for x, y in gears:

        gear_ratio = 1
        scanned = set()
        neighbors = cell_neighbors(x, y, len(lines[x]))

        for n_x, n_y in neighbors:
            if not lines[n_x][n_y].isdigit() and lines[n_x][n_y] == ".":
                continue
            
            left, right = n_y, n_y

            # find the left boundary of the number
            while (lines[n_x][left-1] or "").isdigit():
                left -= 1
            # find the right boundary of the number
            while (lines[n_x][right+1] or "").isdigit():
                right += 1

            if (n_x, left) not in scanned:
                scanned.add((n_x, left))
                part_number = int("".join(lines[n_x][left:right+1]))
                gear_ratio *= part_number
        
        if len(scanned) == 2:
            part_sum += gear_ratio
        
    return part_sum

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_sum(lines))

