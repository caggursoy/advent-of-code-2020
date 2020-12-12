### Part one ###
with open('day9-input.txt', 'r') as fp:
    lines = fp.readlines()
    lines=[int(line.rstrip()) for line in lines]

# print(lines)
def part1(inp_list, len_preamble):
    curr_ind = len_preamble
    aux_list = []
    start = 0
    end = start + len_preamble
    while curr_ind < len(inp_list)-1:
        aux_list = inp_list[start:end]
        if curr_ind > len(aux_list)-1:
            start += 1
            end += 1
            valid = False
            for num1 in aux_list[:-1]:
                for num2 in aux_list[1:]:
                    # print(inp_list[curr_ind], num1, num2)
                    if num1 + num2 == inp_list[curr_ind]:
                        valid = True
                        break
                    else:
                        valid = False
                if valid:
                    break
            if not valid:
                return inp_list[curr_ind]
        curr_ind += 1

print('Part one:',part1(lines,5))

### part two ###
import numpy as np
def part2(inp_list, invalid_num):
    contigous_list = []

    for i in range(0, len(inp_list)-1):
        for j in range(1, len(inp_list)-1):
            stack = np.array(inp_list[i:j])
            if np.sum(stack) == invalid_num:
                print('Part two:', stack.min()+stack.max())
part2(lines, part1(lines, 5))
