import numpy as np
import utils

DAY = 6

lines = utils.read_input(DAY)


def simulate(days):
    fishes = np.zeros(9, dtype=int)
    for line in lines:
        for x in line.split(","):
            fishes[int(x)] += 1

    for _ in range(days):
        new_fishes = fishes[0]
        for j in range(fishes.size - 1):
            fishes[j] = fishes[j+1]
        fishes[-1] = new_fishes
        fishes[-3] += new_fishes
    return fishes

# part 1
utils.print_answer(1, np.sum(simulate(80)))
# part 2
utils.print_answer(2, np.sum(simulate(256)))
