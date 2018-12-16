import os
import numpy as np

fpath = os.path.join('Resources', 'aoc201806_data.txt')
with open(fpath, 'r') as f:
    data = f.read().splitlines()
data = np.array([[int(coord) for coord in coords.split(',')] for coords in data])

x, y = data.T
def get_areas(buffer):
    xs = np.arange(x.min() - buffer, x.max() + buffer)
    ys = np.arange(y.min() - buffer, y.max() + buffer)
    xx, yy = np.meshgrid(xs, ys)
    layers = np.array([np.abs(xx - x_) + np.abs(yy - y_) for x_, y_ in zip(x,y)])
    _, counts = np.unique(layers.argmin(axis=0), return_counts=True)

    return counts



areas = get_areas(100)
print('Part 1: ', areas[areas == get_areas(101)].max())

def get_safe_area(buffer=1):
    xs = np.arange(x.min() - buffer, x.max() + buffer)
    ys = np.arange(y.min() - buffer, y.max() + buffer)
    xx, yy = np.meshgrid(xs, ys)
    layers = np.array([np.abs(xx - x_) + np.abs(yy - y_) for x_, y_ in zip(x,y)])
    return (layers.sum(axis = 0) < 1e4).sum()
print('Part 2: ', get_safe_area())