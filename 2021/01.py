import numpy as np
import utils

DAY = 1

def count_increases(array :np.ndarray) ->int:
    count = 0
    for i in range(1,array.size):
        count += (array[i-1] < array[i])
    return count

lines = utils.read_input(DAY)
data = np.zeros(len(lines), dtype=int)
for i,line in enumerate(lines):
    data[i] = int(line)

# part 1
utils.print_answer(1, count_increases(data))

# part 2
h = 3       # sliding window size
data_sw = np.zeros(data.size - h + 1)
for i in range(data_sw.size):
    data_sw[i] = np.sum(data[i:i+h])

utils.print_answer(2, count_increases(data_sw))
