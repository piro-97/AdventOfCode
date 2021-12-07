import utils
import numpy as np

DAY = 3


def find_most_common_bit(array :np.ndarray) -> int:
    binc = np.bincount(array)    # count each element occurrencies
    return int(binc[1] >= binc[0])


lines = utils.read_input(DAY)
shape = (len(lines), len(lines[0])-1)
values = np.zeros(shape, dtype=int)

for i in range(shape[0]):
    for j in range(shape[1]):
        values[i,j] = int(lines[i][j])

# part 1
gamma = ""
epsilon = ""
for i in range(shape[1]):
    mcb = find_most_common_bit(values[:,i])
    gamma += str(mcb)
    epsilon += str(1 - mcb)

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
utils.print_answer(1, gamma * epsilon)


# part 2
oxygen = np.array(values)
i = 0
while oxygen.shape[0] > 1:
    mcb_i = find_most_common_bit(oxygen[:,i])
    oxygen = oxygen[ oxygen[:,i] == mcb_i ]
    i += 1

dyoxide = np.array(values)
i = 0
while dyoxide.shape[0] > 1:
    lcb_i = 1 - find_most_common_bit(dyoxide[:,i])
    dyoxide = dyoxide[ dyoxide[:,i] == lcb_i ]
    i += 1   

ox = ""
dy = ""
for i in range(shape[1]):
    ox += str(oxygen[0,i])
    dy += str(dyoxide[0,i])

utils.print_answer(2, int(ox,2) * int(dy,2))
