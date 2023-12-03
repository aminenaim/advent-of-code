"""
Advent of Code
Day 3 - Part 1 : https://adventofcode.com/2023/day/3
"""

import re

def lookup_specials(lines: list[str]):
    """
    Given a matrix,
    returns a list of tuples containing coordinates of special chars
    """
    specials = []
    for x, line in enumerate(lines):
        for match in re.finditer(r"(?![0-9.]).", line.strip()):
            specials.append((x, match.start()))
        
    return specials

def cell_neighbors(x, y, matrix_length):
    """
    Given coordinates and a max length,
    returns the list of neighbors a list of tuples with each tuple being coordinates
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
    returns the sum of the part numbers (numbers adjacent to a special char)
    """
    part_sum = 0
    scanned = set()
    specials = lookup_specials(lines)

    
    for x, y in specials:

        neighbors = cell_neighbors(x, y, len(lines[x]))

        for n_x, n_y in neighbors:
            cell_value = lines[n_x][n_y]

            if not cell_value.isdigit() and cell_value == ".":
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
                part_sum += int("".join(lines[n_x][left:right+1]))
        
    return part_sum

with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_sum(lines))

