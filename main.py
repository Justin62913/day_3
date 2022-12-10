import string
from string import ascii_letters

with open('data.txt') as file:
    data = [line for line in file.read().strip().split('\n')]

# print(data)

total = 0
for ruck in data:
    half = len(ruck) // 2

    left = set(ruck[:half])
    right = set(ruck[half:])

    for index, letter in enumerate(ascii_letters):
        if letter in left and letter in right:
            total += index + 1
print(total)

badges = 3
total_badges = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:badges]
    badges += 3

    for index, letter in enumerate(ascii_letters):
        if letter in rucksacks[0] and letter in rucksacks[1] and letter in rucksacks[2]:
            total_badges += index + 1

print(total_badges)