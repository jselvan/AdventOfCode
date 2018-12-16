import os
import numpy as np
import re

fabric = np.zeros([1000,1000])
fpath = os.path.join('Resources', 'aoc201803_data.txt')

def get_info(line):
    segs = line.split()
    x,y = segs[2].split(',')
    x,y = int(x), int(y[:-1])

    w,l = segs[3].split('x')
    w,l = int(w),int(l)
    return x,y,w,l

with open(fpath, 'r') as f:
    for line in f:
        x,y,w,l = get_info(line)
        fabric[x:x+w,y:y+l] += 1

overlap = (fabric > 1).sum()
print(f'The answer to part 1 is {overlap}')

with open(fpath, 'r') as f:
    for line in f:
        x,y,w,l = get_info(line)
        if (fabric[x:x+w,y:y+l] == 1).all():
            print(f'The answer to part 2 is {line.split()[0][1:]}')
            break
    else:
        print('failed part 2')
