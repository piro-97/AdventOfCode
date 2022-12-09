from collections import defaultdict

import numpy as np
import utils

DAY = 9


def dir_to_vector(direction :str) -> np.ndarray:
    switch = {
        "R": [1,0],
        "L": [-1,0],
        "U": [0,1],
        "D": [0,-1],
    }

    return np.array(switch[direction])


lines = utils.read_input(DAY)

knots = np.zeros((10,2))
visits = [defaultdict(int) for _ in range(knots.shape[0])]

for line in lines:
    direction, quantity = line.split()
    direction = dir_to_vector(direction)
    quantity = int(quantity)

    for _ in range(quantity):
        knots[0] += direction

        for i in range(1, knots.shape[0]):
            dist_vector = knots[i-1] - knots[i]

            if np.max(np.abs(dist_vector)) > 1:
                knots[i] += np.clip(dist_vector, -1, 1)

            visits[i][tuple(knots[i])] += 1

utils.print_answer(1, len(visits[1].keys()))
utils.print_answer(2, len(visits[-1].keys()))
