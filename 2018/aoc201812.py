import os
import numpy as np

def run_gen(state, my_rules):
    next_state = set()
    for i in range(min(state) - 3, max(state) + 4):
        segment = ''.join('#' if i + j in state else '.' for j in range(-2,3))
        if segment in my_rules:
            next_state.add(i)
    return next_state

fpath = os.path.join('Resources', 'aoc201812_data.txt')
with open(fpath, 'r') as f:
    state = f.readline().strip('initial state: ').strip('\n')
    f.readline() #dump
    rules = ([rule.split(' => ') for rule in f.read().splitlines()])

state = set(idx for idx, pot in enumerate(state) if pot == '#')
my_rules = set(rule for rule, outcome in rules if outcome == '#')

#50bil my ass
first_few = []
ngens = int(2e2)
for i in range(ngens):
    state = run_gen(state, my_rules)
    first_few.append(sum(state))
    if i == 19:
        print('Part 1:', sum(state))

diff = np.diff(first_few)
print(f'Growth is linear past {np.where(np.diff(diff) == 0)[0][0]}')
print('Extrapolating...')
ans = diff[-1]*(5e10 - ngens) + first_few[-1]
print('Part 2:', int(ans))