import re

def extract_matches(pattern, text):
    matches = re.findall(pattern, text)
    return matches

def extract_numbers(text):
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    return matches

with open("day3_input.txt", "r") as f:
    text = f.read()

# Part 1
pattern = r"mul\(\d{1,3},\d{1,3}\)"
matches = extract_matches(pattern, text)
numbers = [extract_numbers(match) for match in matches]
result = sum([int(num[0]) * int(num[1]) for num in numbers])
print(f"The multiplcation results is: {result}")

# Part 2
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches = extract_matches(pattern, text)
result = 0
execute = True
for match in matches:
    if execute and match[:3] == "mul":
        numbers = extract_numbers(match)
        result += int(numbers[0]) * int(numbers[1])
    elif match[:4] == "do()":
        execute = True
    elif match[:7] == "don't()":
        execute = False
print(f"The multiplcation results with control function is: {result}")