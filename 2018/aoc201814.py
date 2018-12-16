import os
myinput = 939601

recipes = [3,7]
elf1, elf2 = [0,1]
while len(recipes) < myinput+10:
    new_recipes = recipes[elf1] + recipes[elf2]
    recipes.extend(list(map(int,str(new_recipes))))
    elfidx  = [(idx + 1 + recipes[idx]) % len(recipes) for idx in elfidx]

print('Part 1:', "".join(map(str, recipes[-10:])))


recipes = [3,7]
elf1, elf2 = [0,1]
myinput = str(myinput)
while myinput not in ''.join(map(str,recipes[-1-len(myinput):])):
    new_recipes = recipes[elf1] + recipes[elf2]
    recipes.extend(list(map(int,str(new_recipes))))
    elf1, elf2  = (elf1 + 1 + recipes[elf1]) % len(recipes), (elf2 + 1 + recipes[elf2]) % len(recipes)
    
print('Part 2:', ''.join(map(str,recipes)).index(myinput))
