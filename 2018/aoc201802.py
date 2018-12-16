import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201802_data.txt')
with open(fpath, 'r') as f:
    data = f.readlines()

has_twice = 0
has_thrice = 0
for line in data:
    counts = [line.count(char) for char in np.unique([*line])]
    if 2 in counts:
        has_twice += 1
    if 3 in counts:
        has_thrice += 1

print(f'The answer to part 1 is {has_twice * has_thrice}')

data_ord_np = np.array([[ord(char) for char in line if char != '\n'] for line in data])

for i, row in enumerate(data_ord_np):
    find = (np.count_nonzero((data_ord_np - row), axis = 1) == 1)
    if find.any():
        a = np.array([*data[find.argmax()][:-1]])
        b = np.array([*data[i][:-1]])
        print(f'The answer to part 2 is {"".join(a[a==b])}')
        break
else:
    print('failed')