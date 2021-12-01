import os
import re
from collections import deque


def solve(d1, d2):
    while len(d1) > 0 and len(d2) > 0:
        c1 = d1.popleft()
        c2 = d2.popleft()
        if c1 > c2:
            d1.extend((c1,c2))
        else:
            d2.extend((c2,c1))


    return d1 if d1 else d2


f = open(os.getcwd() + '/2020/22/input.txt', 'r')
Lines = f.readlines()

player = 1
deck1 = []
deck2 = []
for line in Lines:
    if line == "\n":
        player = 2
        continue

    if re.match(r"\d+", line):
        if player == 1:
            deck1.append(int(line))
        else:
            deck2.append(int(line))

deck1 = deque(deck1)
deck2 = deque(deck2)

solution = solve(deck1, deck2)
res = 0
for i, num in enumerate(solution):
    print(i, num)
    res += solution[len(solution) - 1 - i] * (i+1)
print(res)