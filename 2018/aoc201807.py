import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201807_data.txt')
with open(fpath, 'r') as f:
    data = f.read().splitlines()

data = np.array([[line.split()[1], line.split()[7]] for line in data])

steps = np.unique(data)
steps_complete = np.zeros(steps.size)

requirements = np.array([np.isin(steps, data[:,0][data[:,1] == step]).astype(float) for step in steps])
order = ''

while requirements.any():
    idx = np.argwhere( ((steps_complete == 0) * (requirements.sum(axis=1) == 0)) )[0]
    steps_complete[idx] += 1
    requirements -= steps_complete
    requirements[requirements < 1] = 0
    order += steps[idx][0]

order += steps[steps_complete==0][0]
print('Part 1:', order)

countdown = np.fromiter(map(ord, steps), dtype = float) - 4
time_passed = 0
requirements = np.array([np.isin(steps, data[:,0][data[:,1] == step]).astype(float) for step in steps])
while countdown.any():
    idx = np.argwhere( ((countdown != 0) * (requirements.sum(axis=1) == 0)) )[:5]
    countdown[idx] -= 1
    requirements -= (countdown == 0).astype(int)
    requirements[requirements < 0] = 0
    time_passed += 1

print('Part 2:', time_passed)