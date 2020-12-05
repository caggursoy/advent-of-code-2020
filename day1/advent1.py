with open('day1-input.txt', 'r', encoding='utf-8') as file:
    inputList = list(map(int, file.readlines()))
flag=True
for p in inputList:
    for q in inputList:
        if p+q == 2020 and flag:
            print('Puzzle answer is for part one is:', p*q)
            flag = False
flag=True
for p in inputList:
    for q in inputList:
        for r in inputList:
            if p+q+r == 2020 and flag:
                print('Puzzle answer is for part two is:', p*q*r)
                flag = False
