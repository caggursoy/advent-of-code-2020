##### Part one #####
inpFile = open('./day6-input.txt')
lineList = []
yesList = ['a','b','c','x','y','z']
yesNum = 0
yesNumList = []
for line in inpFile.read().split('\n\n'):
    lineList.append(line)

for line in lineList:
    line = list(dict.fromkeys(line))
    for char in line:
        if char != '\n':
            yesNum += 1
    yesNumList.append(yesNum)
    yesNum = 0
print('Answer for part one is:',sum(yesNumList))

###### Part two #####
from collections import Counter
total = 0
with open('day6-input.txt') as fp:
    lines=fp.readlines()
groups = []
group = []
for question in lines:
    if question!="\n":
        group.append(question.split("\n")[0])
    else:
        groups.append(group)
        group=[]
groups.append(group)
for group in groups:
    group_size = len(group)
    counts = Counter(''.join(group))
    counts = Counter(list(counts.values()))[group_size]
    total+=counts
print('Answer for part two is:', total)
