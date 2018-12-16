import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201805_data.txt')
with open(fpath, 'r') as f:
    data = f.read().strip()

def react(data):
    stack = []
    for letter in data:
        if stack and letter.lower() == stack[-1].lower() and letter != stack[-1]: 
            stack.pop()
        else:
            stack.append(letter)
    return stack

print(f'The answer to part 1 is {len(react(data))}')

polymer_lengths = []
alphabet = map(chr, range(ord('a'), ord('z') + 1))
for letter in alphabet:
    polymer_lengths.append(len(react(data.replace(letter, '').replace(letter.upper(), ''))))

print(f'The answer to part 2 is {min(polymer_lengths)}')