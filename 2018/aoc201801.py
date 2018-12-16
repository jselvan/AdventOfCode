import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201801_data.txt')
with open(fpath, 'r') as f:
    data = f.readlines()

data = np.fromiter(map(int, data), dtype=int)
print(f'Answer to part 1 is {data.sum()}')

sums = set()
def find_repeat_sum(data, freq, sums):
    for val in data:
        freq += val
        if freq not in sums:
            sums.add(freq)
        else:
            return freq
    else:
        return find_repeat_sum(data, freq, sums)

freq = find_repeat_sum(data, 0, sums)
print(f'Answer to part 2 is {freq}')
