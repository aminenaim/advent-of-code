"""
Advent of Code
Day 9 - Part 1 : https://adventofcode.com/2023/day/9
"""

def parse_histories(lines: list[str]):
    """
    Given a list of histories (strings),
    returns the parsed histories
    """
    return [list(map(int, line.split())) for line in lines]


def predict(history: list[int]):
    """
    Given a history of values,
    return the extrapolated value 
    """
    index = 0
    sequence = [history]
    
    while sum(sequence[index]) != 0:
        sequence.append([sequence[index][i+1]-sequence[index][i] for i in range(len(sequence[index])-1)])
        index += 1

    return sum([s[-1] for s in sequence])
    

def compute_answer(lines: list[str]):
    """
    Given histories of values,
    returns the sum of all the extrapolated values
    """
    histories = parse_histories(lines)

    return sum([predict(h) for h in histories])


with open("input.txt", "r") as file:
    lines = file.readlines()
    print("answer :", compute_answer(lines))
