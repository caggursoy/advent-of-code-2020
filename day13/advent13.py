# ### Part one ###
with open('day13-input.txt', 'r') as fp:
    lines = fp.read().splitlines()

timestamp = int(lines[0])
bus_ids = [int(el) for el in lines[1].split(',') if el != 'x']
remNums = []
for id in bus_ids:
    rem = timestamp%id
    div = timestamp/id
    divNum = id*(int(div)+1)
    remNums.append(divNum-timestamp)

print('Answer to part one is:',bus_ids[remNums.index(min(remNums))]*min(remNums))

### Part two ###
busses = ["x" if x == "x" else int(x) for x in lines[1].split(",")]
print(busses)
rems = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
print(rems)
vals = list(reversed(sorted(rems)))
val = rems[vals[0]]
r = vals[0]
for b in vals[1:]:
    while val % b != rems[b]:
        val += r
    r *= b
print(val)
