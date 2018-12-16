import os
import numpy as np

last_marble = 71035
nplayers = 479
player_scores = np.zeros(nplayers, int)
active_player = -1
circle = np.array([])
idx = 0
for i in range(last_marble+1):
    if i == 0:
        circle = [0]
    elif i == 1:
        idx = 1
        circle.insert(idx, i)
    elif i % 23 == 0:
        player_scores[active_player] += i
        idx -= 7
        idx %= len(circle)
        player_scores[active_player] += circle.pop(idx)
    else:
        idx += 2
        idx %= len(circle)
        circle.insert(idx, i)
    active_player += 1
    active_player %= nplayers

print('Part 1:', player_scores.max())

from collections import deque, defaultdict

def play_game(nplayers, last_marble):
    player_scores = np.zeros(nplayers, int)
    circle = deque([0])
    active_player = idx = 0

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            player_scores[active_player] += marble
            target_index = (idx - 7) % len(circle)
            circle.rotate(-target_index)
            player_scores[active_player] += circle.popleft()
            circle.rotate(target_index - 1)
            circle.rotate(7)
        else:
            circle.append(marble)
            circle.rotate(-1)

        idx = len(circle) - 2
        active_player = (active_player + 1) % nplayers

    return(player_scores.max())

print('Part 2:', play_game(479,71035*100))

pass