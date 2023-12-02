"""
Advent of Code
Day 1 - Part 2 : https://adventofcode.com/2023/day/1
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

def replace_spelled_digits(line: str):
    """
    Given a line, returns the line with spelled out digits replaced by their numeric values
    """
    spelled_out_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i, word in enumerate(spelled_out_digits):
        digit = i + 1
        # replaces every spelled digit by its numeric value
        line = line.replace(word, f'{word}{digit}{word}')

    return line

answer = 0

with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        answer += compute_calibration_value(replace_spelled_digits(line))

print(answer)
