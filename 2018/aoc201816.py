import os
import re
from collections import defaultdict

import numpy as np
from aoc201816_resources import opcode_funs_list

fpath = os.path.join('Resources', 'aoc201816_data.txt')
with open(fpath, 'r') as f:
    samples, test = f.read().split('\n\n\n')
    samples = [[[int(x) for x in re.findall(r'-?\d+', line)] for line in sample.splitlines()] for sample in samples.split('\n\n')]
    test = [[int(x) for x in re.findall(r'-?\d+', line)]  for line in test.splitlines()[1:]]

#this default dict initializes with a set containing a value for any possible function index
opcode_map = defaultdict(lambda: set(range(len(opcode_funs_list))))

counter = 0
for before, (opcode, a,b,c), after in samples:
    behaves_like = np.array([1 if fun(before.copy(), a, b, c) == after else 0 for fun in opcode_funs_list])
    if behaves_like.sum() >= 3:
        #to solve for p1
        counter += 1
    #return the overlap between possible function indices every time we encounter a given opcode
    opcode_map[opcode] &= set(np.where(behaves_like)[0])

opcode_funs_dict = {}
while opcode_map:
    #loop through opcode map until we have mapped each opcode to a function
    only_one = [k for k, v in opcode_map.items() if len(v) == 1]
    #we find all the opcodes that only have one function index associated
    for opcode in only_one:
        #pop out the index associated with given opcode
        idx = list(opcode_map.pop(opcode))[0]
        #retrieve the associated function and add it to opcode funs dict
        opcode_funs_dict[opcode] = opcode_funs_list[idx]
        #remove this function index from every other entry
        for k in opcode_map:
            opcode_map[k].discard(idx)

r = [0,0,0,0]
for (opcode, a, b, c) in test:
    r = opcode_funs_dict[opcode](r,a,b,c)

print('Part 1:', counter)
print('Part 2:', r[0])