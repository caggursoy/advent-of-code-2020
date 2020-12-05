## part 1
with open('day2-input.txt', 'r', encoding='utf-8') as file:
    inputList = list(file.readlines())
minList = []
maxList = []
charList = []
strList = []
validKeys = 0
for line in inputList:
    ind0 = line.find('-')
    ind1 = line.find(' ')
    ind2 = line.rfind(' ')
    minList.append(int(line[:ind0]))
    maxList.append(int(line[ind0+1:ind1]))
    charList.append(line[ind1+1:ind1+2])
    strList.append(line[ind2+1:-1])
for i in range(len(inputList)):
    cnt = strList[i].count(charList[i])
    if cnt >= minList[i] and cnt <= maxList[i]:
        validKeys += 1
print('Answer of part 1:',validKeys)

## part 2
validKeys2 = 0
for i in range(len(inputList)):
    if bool(strList[i][minList[i]-1] == charList[i]) ^ bool(strList[i][maxList[i]-1] == charList[i]):
        validKeys2 += 1
print('Answer of part 2:',validKeys2)
