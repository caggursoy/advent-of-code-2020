##### Part one #####
inpFile = open('./day5-input.txt')
rows = range(0,128)
len_rows = len(rows)
cols = range(0,8)
len_cols = len(cols)
lineList = []
seat_id_list = []
for line in inpFile.read().split('\n'):
    lineList.append(line)
lineList = lineList[:-1]

for line in lineList:
    for ch in line:
        if ch == 'F':
            rows = rows[:(len_rows/2)]
            len_rows = len(rows)
        elif ch == 'B':
            rows = rows[(len_rows/2):]
            len_rows = len(rows)
        elif ch == 'L':
            cols = cols[:(len_cols/2)]
            len_cols = len(cols)
        elif ch == 'R':
            cols = cols[(len_cols/2):]
            len_cols = len(cols)
        if len_cols <= 1 and len_rows <= 1:
            # print('Found solution for',line)
            # print('Rows:',rows)
            # print('Cols:',cols)
            seat_id = rows[0]*8+cols[0]
            seat_id_list.append(seat_id)
            # print('Seat ID: ',seat_id)
            rows = range(0,128)
            len_rows = len(rows)
            cols = range(0,8)
            len_cols = len(cols)
            break
print('Maximum id is:',max(seat_id_list))

### Part two ###
sorted_id_list = sorted(seat_id_list)
for id in sorted_id_list:
    if id+1 and id-1 in sorted_id_list:
        continue
    elif id == sorted_id_list[0]:
        continue
    else:
        print('The seat number is:',id-1)
