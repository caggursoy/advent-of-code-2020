### Part one ###
with open('day8-input.txt', 'r') as fp:
    lines = fp.readlines()
    lines=[line.rstrip() for line in lines]

def part1(lines):
    curr_acc = 0
    curr_line = 0
    valid = True
    prev_lines = set()
    while True:
        if len(lines)-1 == curr_line:
            valid = False
        if curr_line in prev_lines:
            valid = False
            return curr_acc, valid

        op, acc = lines[curr_line].split(' ')
        acc = int(acc)
        prev_lines.add(curr_line)

        if op == 'nop':
            curr_line += 1
        elif op == 'acc':
            curr_acc += acc
            curr_line += 1
        elif op == 'jmp':
            curr_line += acc

        if valid == False:
            return curr_acc, True
    return curr_acc, False
print('Answer to part one:', part1(lines)[0])

### Part two ###
def part2(lines):
    curr_acc = 0
    curr_line = 0
    visited = []
    aux_lines = lines.copy()
    for curr_line in range(1, len(aux_lines)):
        op, acc = lines[curr_line].split(" ")
        acc = int(acc)
        if op == 'nop':
            op = 'jmp'
        elif op == 'jmp':
            op = 'nop'
        visited = []
        aux_lines = lines.copy()
        aux_lines[curr_line] = ' '.join((op, str(acc)))
        acc, valid = part1(aux_lines)
        if valid:
            return acc
print('Answer to part two:', part2(lines))
