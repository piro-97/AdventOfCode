import numpy as np
import utils

DAY = 7


def fuel_needed(initial_positions :np.ndarray, destination :int) -> int:
    return np.sum(np.abs(initial_positions - destination))

def fuel_needed_2(initial_positions :np.ndarray, destination :int) -> int:
    n = np.abs(initial_positions - destination)
    return np.sum(n * (n+1) / 2)

lines = utils.read_input(DAY)

# part 1
for line in lines:
    positions = [int(x) for x in line.split(",")]
positions = np.array(positions, dtype=int)

max_pos = np.max(positions)
min_pos = np.min(positions)

fuel_consumption = np.zeros((max_pos - min_pos + 1), dtype=int)
for i in range(min_pos, max_pos + 1):
    fuel_consumption[i] = fuel_needed(positions, i)

utils.print_answer(1, np.min(fuel_consumption))

# part 2
fuel_consumption = np.zeros((max_pos - min_pos + 1), dtype=int)
for i in range(min_pos, max_pos + 1):
    fuel_consumption[i] = fuel_needed_2(positions, i)

utils.print_answer(2, np.min(fuel_consumption))
