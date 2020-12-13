### Part one ###
with open('day11-input.txt', 'r') as fp:
    lines = fp.read().splitlines()
lines = [list(r) for r in lines]

row, col = len(lines), len(lines[0])
d_check = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def num_occup(matrix,i,j):
    res = 0
    row, col = len(lines), len(lines[0])
    for d_i, d_j in d_check:
        I,J = i+d_i,j+d_j
        if 0 <= I < row and 0 <= J < col and matrix[I][J]=='#':
            res += 1
    return res

while True:
    end_flag = True
    lines_aux = [line.copy() for line in lines]
    for i,r in enumerate(lines_aux):
        for j,c in enumerate(r):
            count = num_occup(lines_aux,i,j)
            if c == 'L' and count == 0:
                lines[i][j] = '#'
            elif c == '#' and count >= 4:
                lines[i][j] = 'L'
            end_flag &= (r[j] == lines[i][j])
    if end_flag:
        break
ans=0
for i in range(row):
    for j in range(col):
        if lines[i][j]=='#':
            ans+=1
print('Answer of part one is:',ans)
#
# ### Part two ###
# with open('day11-input.txt', 'r') as fp:
#     lines = fp.read().splitlines()
# lines = [list(r) for r in lines]
#
# row, col = len(lines), len(lines[0])
# d_check = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
#
# def num_occup2(matrix,i,j):
#     res = 0
#     row, col = len(lines), len(lines[0])
#     for d_i, d_j in d_check:
#         I, J = i+d_i, j+d_j
#         while 0 <= I < row and 0 <= J < col:
#             print(I,J,end='\r')
#             if matrix[I][J]=='#':
#                 res+=1
#                 break
#             elif matrix[I][J]=='L':
#                 break
#             I += d_i
#             J += d_j
#     return res
#
# while True:
#     end_flag = True
#     lines_aux = [line.copy() for line in lines]
#     for i,r in enumerate(lines_aux):
#         for j,c in enumerate(r):
#             count = num_occup2(lines_aux,i,j)
#             if c == 'L' and count == 0:
#                 lines[i][j] = '#'
#             elif c == '#' and count >= 4:
#                 lines[i][j] = 'L'
#             end_flag &= (r[j] == lines[i][j])
#     if end_flag:
#         break
# ans=0
# for i in range(row):
#     for j in range(col):
#         if lines[i][j]=='#':
#             ans+=1
# print('Answer of part two is:',ans)

with open('day11-input.txt','r') as f:
    grid=f.read().splitlines()
grid=[list(r) for r in grid]

m,n=len(grid),len(grid[0])

def occupied(grid,i,j):
    ret=0
    m,n=len(grid),len(grid[0])
    for di,dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        I,J=i+di,j+dj
        while 0<=I<m and 0<=J<n:
            if grid[I][J]=='#':
                ret+=1
                break
            elif grid[I][J]=='L':
                break
            I+=di
            J+=dj
    return ret

while True:
    stable=True
    grid_c=[r.copy() for r in grid]
    for i,r in enumerate(grid_c):
        for j,c in enumerate(r):
            count=occupied(grid_c,i,j)
            if c=='L' and count==0:
                grid[i][j]='#'
            elif c=='#' and count>=5:
                grid[i][j]='L'
            stable&=(r[j]==grid[i][j])
    if stable:
        break

ans=0
for i in range(m):
    for j in range(n):
        if grid[i][j]=='#':
            ans+=1
print(ans)
