"""
Advent of Code
Day 1 - Part 1: https://adventofcode.com/2023/day/1
"""

import re

def compute_calibration_value(line: str):
    """
    Given a line, returns the calibration value 
    (first and last digit to form a two-digit number)
    """
    # filters out digits from the line
    digits = re.sub(pattern='[^0-9]', repl='', string=line)

    # form a two(digit number using first and last digit
    calibration_value = int(f'{digits[0]}{digits[-1]}')

    return calibration_value

answer = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        answer += compute_calibration_value(line)

print(answer)
