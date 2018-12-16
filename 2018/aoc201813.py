import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201813_data.txt')
with open(fpath, 'r') as f:
    data = [list(line) for line in f.read().splitlines()]

carts = {
    '>':[0,1],
    '<':[0,-1],
    '^':[-1,0],
    'v':[1,0]
}

mycarts = []
for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val in carts:
            mycarts.append([y,x] + carts[val] + [0])

p1done = False
crashed = set()
while True:
    for i, cart in enumerate(mycarts):
        [y, x, dy, dx, r] = cart
        y += dy
        x += dx
        
        path = data[y][x]
        if path == '\\':
            dx, dy = dy, dx
        elif path == '/':
            dx, dy = -dy, -dx
        elif path == '+':
            if r == 0:
                dx, dy = dy, -dx
            elif r == 2:
                dx, dy = -dy, dx
            r += 1
            r %= 3

        crashed_this_time = {j for j, (oy, ox, _,_,_) in enumerate(mycarts) if y == oy and x == ox}
        if crashed_this_time:
            if not p1done:
                print(f'Part 1: {x},{y}')
                p1done = True
            crashed.add(i)
            crashed |= crashed_this_time
        else:            
            mycarts[i] = [y,x,dy,dx,r]
    else:
        mycarts = [cart for k, cart in enumerate(mycarts) if k not in crashed]
        crashed = set() 
        
        if len(mycarts) > 1:
            mycarts.sort()
        else:
            y,x,_,_,_ = mycarts[0]
            print(f'Part 1: {x},{y}')
            break