import os
import numpy as np
import pandas as pd 

# [1518-05-04 23:58] Guard #2657 begins shift
# [1518-09-09 00:06] falls asleep
# [1518-06-04 00:32] wakes up

fpath = os.path.join('Resources', 'aoc201804_data.txt')
data = {}
with open(fpath, 'r') as f:
    data = np.array(sorted([line[1:-1].split('] ') for line in f], key = lambda x: x[0]))
shifts = np.split(data, np.where(np.char.find(data, 'Guard') == 0)[0])

sleeping_patterns = {}
for shift in shifts[1:]:
    guard_id = int(shift[0,1].replace('Guard #','').replace(' begins shift', ''))
    date = shift[0,0].split()[0]
    toggle_sleep = [int(time[-2:]) for time in shift[1:,0]]
    sleep = []
    status = 0
    for i in range(60):
        if i in toggle_sleep:
            status = int(not status)
        sleep.append(status)
    sleeping_patterns[(guard_id, date)] = sleep

df = pd.DataFrame(sleeping_patterns).T
df.index.names = ['guard_id', 'date']
df.groupby('guard_id').sum()

guard_most_sleep = df.groupby('guard_id').sum(axis = 1).sum(axis = 1).idxmax()
minute_most_sleep = df.groupby('guard_id').sum(axis = 1).loc[guard_most_sleep].idxmax()
print(f'answer to part 1 is {guard_most_sleep*minute_most_sleep}') 

guard_most_sleep = df.groupby('guard_id').sum().max(axis=1).idxmax()
minute_most_sleep = df.groupby('guard_id').sum().max(axis=0).idxmax()
print(f'answer to part 2 is {guard_most_sleep*minute_most_sleep}') 