from typing import Iterator
import utils
from collections import defaultdict
from itertools import product

DAY = 20

ITER_1 = 2
ITER_2 = 50


def neighbours(index :tuple) -> list:
    x,y = index
    return list(product([x-1, x, x+1], [y-1, y, y+1]))


def out_val(input :dict, index :tuple, algo :list) -> bool:
    b = ""
    ne = neighbours(index)
    for n in ne:
        b += str(int(input[n]))
    return algo[int(b,2)]


def find_points(values :"list[tuple]") -> Iterator:
    X = list(map(lambda x : x[0], values))
    Y = list(map(lambda x : x[1], values))
    min_x, max_x, min_y, max_y = min(X), max(X), min(Y), max(Y)
    return product(range(min_x-1, max_x+2), range(min_y-1, max_y+2))

    
lines = utils.read_input(DAY)

algo = list(map(lambda x : x == "#", lines[0]))
switch = False
input = defaultdict(bool)
for i,line in enumerate(lines[2:]):
    for j,c in enumerate(line):
        input[(i,j)] = (c == "#")

if algo[0] and algo[-1]:
    print("the answer is: infty")
    exit(0)

for i in range(ITER_2):
    out = defaultdict(lambda : switch)
    points = find_points(input.keys())
    for p in points:
        out[p] = out_val(input, p, algo)
    input = out
    if algo[0]:
        switch = not switch
    
    # part 1
    if i == ITER_1 - 1:
        utils.print_answer(1, sum(out.values()))

# part 2
utils.print_answer(2, sum(out.values()))
