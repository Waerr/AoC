import re

with open('input.txt', 'r') as f:
    input = f.readlines()


def part_one():
    total = 0
    for line in input:
        first_digit, *_, last_digit = re.findall(r'\d', line * 2)
        total += int(first_digit + last_digit)   
    return total


def part_two():
    digits = {'1': '1', 
            'one': '1', 
            '2': '2', 
            'two': '2', 
            '3': '3', 
            'three': '3', 
            '4': '4', 
            'four': '4', 
            '5': '5', 
            'five': '5', 
            '6': '6', 
            'six': '6', 
            '7': '7', 
            'seven': '7', 
            '8': '8', 
            'eight': '8', 
            '9': '9', 
            'nine': '9'}
    total = 0
    for line in input:
        first_digit, *_, last_digit = re.findall(rf"(?=({'|'.join(digits)}))", line * 2)
        total += int(digits[first_digit] + digits[last_digit])
    
    return total


print(part_one())        
print(part_two())


