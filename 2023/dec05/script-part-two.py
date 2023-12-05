"""
Advent of Code
Day 5 - Part 2 : https://adventofcode.com/2023/day/5
--
Naive method, also called "turn you laptop into a toaster 101"
"""

def parse_categories(lines: str):
    """
    Given a list of strings,
    returns a tuple (seeds, maps)
    """
    map = ""
    seeds = []
    maps = {}   # dicts beings insertion ordered, I chose to use them
    
    for line in lines:

        line = line.strip()

        if line.startswith("seeds"):
            seeds = [int(n) for n in line.split(":")[1].split()]
            continue
        elif line.endswith("map:"):
            map = line.split()[0]
            maps[map] = []
        elif line == "":
            continue
        else:
            maps[map].append([int(n) for n in line.split()])
    
    return seeds, maps

def transform(number: int, map: list[list[int]]):
    """
    Given a number and a map,
    returns the transformed value
    """

    for ranges in map:
        dest, source, length = ranges
        if source <= number and number < source+length:
            number = number-source+dest
            break

    return number

def compute_location(seed: int, maps: dict[str]):
    """
    Given a seed number and maps dictionnary,
    returns the computed location value  
    """
    number = seed
    for v in maps.values():
        number = transform(number, v)
    return number


def compute_lowest_location(lines: list[str]):
    """
    Given a list of seeds number and maps,
    returns the the lowest seed location
    """
    seeds, maps = parse_categories(lines)

    seeds_range = set()
    for start, ranges in zip(seeds[0::2], seeds[1::2]):
        for seed_number in range(start, start+ranges):
            seeds_range.add(seed_number)

    return min([compute_location(s, maps) for s in seeds_range])


with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_lowest_location(lines))

