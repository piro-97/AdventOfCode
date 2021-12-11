from itertools import product
import numpy as np
import utils

DAY = 11

DIM = 10
ITER = 100


def neighbours(index :tuple) -> np.ndarray:
    x, y = index
    if x == 0:
        l_x = [x, x+1]
    elif x == DIM-1:
        l_x = [x-1, x]
    else:
        l_x = [x-1, x, x+1]
    
    if y == 0:
        l_y = [y, y+1]
    elif y == DIM-1:
        l_y = [y-1, y]
    else:
        l_y = [y-1, y, y+1]
    
    n = set( product( l_x, l_y ) )
    n.remove((x,y))
    return n
    
def step(matrix :np.ndarray) -> int:
    matrix += 1
    flashed = np.zeros_like(matrix, dtype=bool)

    while(np.any(matrix > 9)):
        for index in np.argwhere(matrix > 9):
            x,y = index
            if not flashed[x,y]:
                flashed[x,y] = True
                ne = neighbours((x,y))
                for n in ne:
                    matrix[n] += 1
            matrix *= (1-flashed)

    return np.sum(flashed)


lines = utils.read_input(DAY)

octopuses = np.zeros((DIM,DIM), dtype=int)

for i, line in enumerate(lines):
    for j, n in enumerate(line):
        octopuses[i,j] = n

octo_2 = octopuses.copy()

# part 1
flashes = 0
for _ in range(ITER):
    flashes += step(octopuses)
    
utils.print_answer(1, flashes)

# part 2
i = 0
while True:
    step(octo_2)
    if np.sum(octo_2) == 0:
        utils.print_answer(2, i+1)
        break
    i += 1