import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201808_data.txt')
with open(fpath, 'r') as f:
    data = f.read().split()

data = np.fromiter(map(int, data), int)

def read_data(data, metadata_val):
    idx = 2
    if data.size < 2:
        return metadata_val
    nchildren, nmetadata = data[:idx]
    for _ in range(nchildren):
        metadata_val, idx_ = read_data(data[idx:], metadata_val)
        idx += idx_
    end = idx + nmetadata
    metadata_val += data[idx:end].sum()
    return metadata_val, end

print('Part 1:', read_data(data, 0)[0])

tree = {}
def parse_data(data, my_tree):
    idx = 2
    nchildren, nmetadata = data[:idx]
    my_tree['children'] = []
    for i in range(nchildren):
        my_tree['children'].append({})
        idx += parse_data(data[idx:], my_tree['children'][i])
    end = idx + nmetadata
    metadata_val = data[idx:end]
    my_tree['metadata'] = metadata_val
    return end

def walk_tree(tree):
    rolling_sum = 0
    nchildren = len(tree['children']) 
    if nchildren == 0:
        return tree['metadata'].sum()
    else:
        for i in tree['metadata']:
            i -= 1
            if i < nchildren:
                rolling_sum += walk_tree(tree['children'][i])
    return rolling_sum

parse_data(data, tree)

print('Part 2:', walk_tree(tree))