"""
Advent of Code
Day 9 - Part 2 : https://adventofcode.com/2023/day/9
"""
from functools import reduce
import operator

def parse_histories(lines: list[str]):
    """
    Given a list of histories (strings),
    returns the parsed histories
    """
    return [list(map(int, line.split())) for line in lines]


def predict(history: list[int]):
    """
    Given a history of values,
    return the backward extrapolated value 
    """
    index = 0
    sequence = [history]
    
    while sum(sequence[index]) != 0:
        sequence.append([sequence[index][i+1]-sequence[index][i] for i in range(len(sequence[index])-1)])
        index += 1

    for i in range(start=len(sequence)-2, stop=-1, step=-1):
        # computing the above backward extrapolated value
        sequence[i].insert(0, sequence[i][0]-sequence[i+1][0])

    return sequence[0][0]
    

def compute_answer(lines: list[str]):
    """
    Given histories of values,
    returns the sum of all the backwards extrapolated values
    """
    histories = parse_histories(lines)

    return sum([predict(h) for h in histories])


with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))
