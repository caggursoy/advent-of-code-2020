### Part one ###
with open('day10-input.txt', 'r') as fp:
    lines = fp.readlines()
    lines=[int(line.rstrip()) for line in lines]

one_jolt = 0
two_jolt = 0
three_jolt = 0
outlet_rating = 0

lines.append(max(lines)+3)

while True:
    if (outlet_rating + 1) in lines:
        one_jolt += 1
        outlet_rating += 1
    elif outlet_rating + 2 in lines:
        two_jolt+=1
    elif outlet_rating + 3 in lines:
        three_jolt += 1
        outlet_rating += 3
    else:
        break
print('Part one solution:', one_jolt*three_jolt)

### Part two ###

solution = {0:1} # initial case
for line in sorted(lines):
    solution[line] = 0
    if line - 1 in solution:
        solution[line] += solution[line-1]
    if line - 2 in solution:
        solution[line] += solution[line-2]
    if line - 3 in solution:
        solution[line] += solution[line-3]

print(solution[max(lines)])
