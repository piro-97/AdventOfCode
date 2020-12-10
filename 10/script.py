import os


def get_predecessors(list, index):
    p = []
    for j in [1,2,3]:
        if index - j >= 0 and \
        0 <= list[index] - list[index - j] <= 3:
            p.append(list[index - j]) 
    return p



f = open(os.getcwd() + "/10/input.txt", "r")
Lines = f.readlines()

adapters_sorted = list((int(line) for line in Lines))
adapters_sorted.sort()


# part 1

last_adapter_jolts = 0
one_jolt_diff = 0
two_jolts_diff = 0
three_jolts_diff = 0

i = 0
while i < len(adapters_sorted):
    diff = adapters_sorted[i] - last_adapter_jolts
    if diff > 3:
        print('difference of power is too high')
    if diff == 3:
        three_jolts_diff += 1
    if diff == 2:
        two_jolts_diff += 1
    if diff == 1:
        one_jolt_diff += 1

    last_adapter_jolts = adapters_sorted[i]
    i += 1

three_jolts_diff += 1   # my device

print("part 1: " + str(one_jolt_diff * three_jolts_diff))


# part 2

adapters_sorted.insert(0, 0)

ways_to_get_here = {}   # for each adapter count how many ways we have to get there from its predecessors


for i, adapter in enumerate(adapters_sorted):
    predecessors = get_predecessors(adapters_sorted, i)

    if adapter == 0:
        ways_to_get_here[adapter] = 1
    else:
        ways_to_get_here[adapter] = 0

    for p in predecessors:
        ways_to_get_here[adapter] += ways_to_get_here[p]

indes_of_last = list(ways_to_get_here)[-1]
print("part 2: " + str(ways_to_get_here[indes_of_last]))