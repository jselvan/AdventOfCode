import os
import numpy as np

serial_number = 8

def get_power(x,y,s):
    p = (((((x+10) * y + s) * (x+10)) // 100 ) % 10) - 5
    return p

l = 300
r = np.arange(l) + 1
x,y = np.meshgrid(r,r)
s = 9424
p = get_power(x,y,s).T


max_power = 0
for size in range(3,30): #picked 30 cause around there things started becoming negative
    w = l - size + 1
    pcells = sum([p[x_:x_+w,y_:y_+w] for y_ in range(size) for x_ in range(size)])
    if max_power < pcells.max():
        max_power = pcells.max()
        idx = np.where(pcells == pcells.max())
        ans = f'{idx[0][0]+1},{idx[1][0]+1},{size}\nmax = {pcells.max()}'
    if size == 3:
        print(f'Part 1: {idx[0][0]+1},{idx[1][0]+1}')

print('Part 2:', ans)