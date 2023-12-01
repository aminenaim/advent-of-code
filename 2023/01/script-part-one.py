"""
Advent of Code
Day 1 - Trebuchet?! : https://adventofcode.com/2023/day/1
Part One
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

computed_puzzle = []

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        calibrationValue = compute_calibration_value(line)
        computed_puzzle.append(calibrationValue)

answer = sum(computed_puzzle)        

print(answer)
