import os
import numpy as np
import re

fpath = os.path.join('Resources', 'aoc201810_data.txt')
with open(fpath, 'r') as f:
    data = f.read().splitlines()
    
data = np.array([[int(x) for x in re.findall(r'-?\d+', line)] for line in data])
x,y,xd,yd = data.T

max_i = int(5e5)
max_d = [np.ptp(x + y + i*(xd + yd)) for i in range(max_i)]
best_i = np.argmin(max_d)

def plot(x,y,i):
    x += i * xd
    y += i * yd
    x -= x.min()
    y -= y.min()
    grid  = np.zeros([x.max()+1, y.max()+1])
    for x_, y_ in zip(x,y): 
        grid[x_,y_] = 1

    print('\n'.join([''.join(['#' if c else ' ' for c in l]) for l in grid.T]))

print('Part 1:')
plot(x,y,best_i)
print('Part 2:', best_i)

pass