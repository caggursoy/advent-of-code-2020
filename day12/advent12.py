### Part one ###
with open('day12-input.txt', 'r') as fp:
    lines = fp.read().splitlines()

curr_state = {'N':0, 'S':0, 'E':0, 'W':0}
curr_dir = 'E'

for line in lines:
    comm = line[0]
    amount = int(line[1:])
    if comm == 'F':
        curr_state[curr_dir] += amount
    elif comm == 'R':
        av = ['E','S','W','N']
        angle = amount
        v = int(angle/90)
        ndir = (av.index(curr_dir)+v) % len(av)
        ndir = av[ndir]
        curr_dir = ndir
    elif comm == 'L':
        av = ['E','N','W','S']
        angle = amount
        v = int(angle/90)
        ndir = (av.index(curr_dir)+v) % len(av)
        ndir = av[ndir]
        curr_dir = ndir

    elif comm == 'N':
        curr_state[comm] += amount
    elif comm == 'S':
        curr_state[comm] += amount
    elif comm == 'W':
        curr_state[comm] += amount
    elif comm == 'E':
        curr_state[comm] += amount
    # print(line,curr_state,curr_dir)
man_dist = abs(curr_state['E'] - curr_state['W']), abs(curr_state['N'] - curr_state['S'])
print('Manhattan distance is:',man_dist,':',man_dist[0]+man_dist[1])

### Part two ###
import math
coord = {'x': 0, 'y': 0}
waypoint = {'x': 10, 'y': 1}

def rotate(origin, point, angle):
    # source: https://stackoverflow.com/a/34374437
    ox, oy = origin
    px, py = point
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return int(round(qx)), int(round(qy))

for line in lines:
    comm = line[0]
    amount = int(line[1:])
    if comm == 'N':
        waypoint['y'] += amount
    elif comm == 'S':
        waypoint['y'] -= amount
    elif comm == 'E':
        waypoint['x'] += amount
    elif comm == 'W':
        waypoint['x'] -= amount
    elif comm == 'F':
        coord['y'] += waypoint['y'] * amount
        coord['x'] += waypoint['x'] * amount
    elif comm in ['L', 'R']:
        if comm == 'R':
            amount = -amount
        waypoint['x'], waypoint['y'] = rotate(
            (0, 0), (waypoint['x'], waypoint['y']), math.radians(amount)
        )
print('Manhattan distance is:',coord,abs(coord['x']) + abs(coord['y']))
