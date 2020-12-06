import numpy as np
## part 1
map = []
numTree = 0
flag = True
i = 0
j = 0
with open('day3-input.txt', 'r', encoding='utf-8') as file:
    mapAux = list(file.readlines())
for line in mapAux:
    map.append([p for p in line[:-1]])
dims = [len(map), len(map[0])]
for k in range(len(map)):
    ind0 = i
    ind1 = (3*k)%dims[1]
    if map[ind0][ind1] == '#':
        numTree += 1
    i += 1
    j += 1

print('Answer for part 1:',numTree)

## part 2
i = 0
j = 0
numTree = 0
numList = []
slopes = [[1,1],[1,3],[1,5],[1,7],[2,1]]
for slope in slopes:
    print(slope)
    for k in range(len(map)):
        if slope[0] == 1 and slope[1] == 1:
            ind0 = i % dims[0]
            ind1 = j % dims[1]
            if map[ind0][ind1] == '#':
                numTree += 1
            i += 1
            j += 1
        elif slope[0] == 1 and slope[1] != 1:
            ind0 = i
            ind1 = (slope[1]*k)%dims[1]
            if map[ind0][ind1] == '#':
                numTree += 1
            i += 1
            j += 1
        elif slope[0] == 2 and slope[1] == 1:
            ind0 = i % dims[0]-1
            ind1 = j % dims[1]
            # print(ind0,ind1,map[ind0][ind1])
            if map[ind0][ind1] == '#':
                numTree += 1
            i += 2
            j += 1
    numList.append(numTree)
    print(numTree)
    numTree = 0
    i = 0
    j = 0
print(np.prod(numList))

## found an answer from internet, in my solution only the last slope is wrong
from functools import reduce

with open('./day3-input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

width = len(puzzle_input[0])
height = len(puzzle_input)

def tree_at_coord(x, y):
    return puzzle_input[y][x%width] == '#'

def trees_encountered(step_x, step_y):
    x,y,count = 0,0,0
    while y < height-1:
        x+=step_x
        y+=step_y
        count += tree_at_coord(x,y)
    return count
# Part 1 ####################################################################
print('Trees encountered:', trees_encountered(3,1))
# Part 2 ####################################################################
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
prod_of_slopes = reduce(lambda a,b: a*trees_encountered(*b), slopes, 1)
print('Product of trees, on all slopes:', prod_of_slopes)
for sl in slopes:
    print(trees_encountered(sl[0],sl[1]))
