from collections import deque
import networkx as nx
import numpy as np
import os

class Unit:
    def __init__(self, name, y, x, dmg=3):
        self.name = name
        self.pos = (y,x)
        self.hp = 200
        self.dmg = dmg
    
    @property
    def alive(self):
        return self.hp > 0

    def attack(self, other):
        other.hp -= self.dmg


def get_neighbours(pos):
    x,y = pos
    offset = [(1,0), (-1,0), (0,1), (0,-1)]
    return [(x+dx, y+dy) for dx,dy in offset]

def run_game(elfpower, part2):
    fpath = os.path.join('Resources', 'aoc201815_data.txt')
    with open(fpath, 'r') as f:
        data = f.read().splitlines()
        data = np.array(list(map(list,data)))

    units = []
    for name in 'GE':
        Y, X = np.where(data == name)
        data[Y,X] = '.'
        units.extend(
            [Unit(name, y, x, 3 if name == 'G' else elfpower)
            for y,x in zip(Y, X)]
        )
    
    iter_data = (
        (y,x,val) for y, row in enumerate(data)
        for x, val in enumerate(row)
    )

    gamemap = nx.Graph()
    ymax, xmax = data.shape
    for y,x,val in iter_data:
        if val =='.':
            valid_neighbours = [
                [(y,x),(ny,nx)] for ny,nx in get_neighbours((y,x)) 
                if (0 <= nx < xmax) and (0 <= ny < ymax) and data[ny,nx] == '.'
            ]
            gamemap.add_edges_from(valid_neighbours)
    
    nturns = 0
    while True:
        # print(nturns)
        units.sort(key=lambda unit:unit.pos)
        for idx, unit in enumerate(units):
            moved = False
            if not unit.alive:
                continue
            
            #everywhere on map there is something that isn't this unit
            occupied = set(
                (u.pos for u in units 
                if u.alive and u != unit)
            ) 
            
            #all units with name not matching this unit
            enemies = [
                enemy for enemy in units
                if enemy.name != unit.name and enemy.alive
            ] 
            
            #a set of all locations that are in range of an enemy
            targets = set(
                (pos for enemy in enemies 
                for pos in get_neighbours(enemy.pos) 
                if data[pos] == '.' and pos not in occupied)
            )

            #the locations around out unit
            nearby = set(
                (pos for pos in get_neighbours(unit.pos)
                if pos in gamemap)
            ) 

            if not targets:
                #there are no target locations, go to the next unit
                continue

            if unit.pos not in targets:
                #unit is not in range so it moves
                newmap = gamemap.copy()
                newmap.remove_nodes_from(occupied)
                distances = nx.shortest_path_length(
                    G = newmap,
                    source = unit.pos
                )
                lengths_to_targets = [
                    [v, k] for k, v in distances.items()
                    if k in targets
                ]
                if not lengths_to_targets:
                    continue

                d, end = min(lengths_to_targets)
                nearby_unoccupied = sorted(list(nearby - occupied))
                for start in nearby_unoccupied:
                    try:
                        dist = nx.shortest_path_length(
                            G = newmap,
                            source = start,
                            target= end
                        )
                    except nx.exception.NetworkXNoPath:
                        continue
                    else:
                        if dist == d - 1:
                            unit.pos = start
                            moved = True
                            break
                        
            if moved:
                #update nearby locations
                nearby = set((pos for pos in get_neighbours(unit.pos))) 
            
            if unit.pos in targets:
                #unit attacks
                nearby_enemies = [enemy for enemy in enemies if enemy.pos in nearby]
                
                #find lowest health enemy in the right order
                target_enemy = min(
                    nearby_enemies, 
                    key = lambda enemy: (enemy.hp, enemy.pos)
                )
                unit.attack(target_enemy)

                if part2 and not target_enemy.alive and target_enemy.name == 'E':
                    return True, 0

                if len(set(u.name for u in units if u.alive)) == 1:
                    #there is only one team with living units left
                    if idx == len(units) - 1:
                        #off by one error?
                        nturns += 1

                    return False, nturns * sum(u.hp for u in units if u.alive)
        nturns += 1

print('Part 1:', run_game(elfpower = 3, part2 = False)[1])

i = 3
elf_dies = True
while elf_dies:
    elf_dies, score = run_game(i, True)
    i += 1
print('Part 2:', score)
pass