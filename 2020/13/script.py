import os
import math
import numpy as np


f = open(os.getcwd() + "/2020/13/input.txt", "r")
Lines = f.readlines()

my_ts = int(Lines[0])

busses = []
l = Lines[1].split(",")
for i, ts in enumerate(l):
    if ts != 'x':
        o = {
            'id' : int(ts),
            'offset' : i % int(ts)
        }
        busses.append(o)


# part 1

next_ts_bus = []
for b in busses:
    bus = b['id']
    next_ts = (math.floor(my_ts / bus) + 1) * bus
    next_ts_bus.append(next_ts)

next_bus = min(next_ts_bus)
next_bus_id = busses[next_ts_bus.index(next_bus)]['id']
answer = next_bus_id * (next_bus - my_ts)
print("part 1: " + str(answer))


# part 2

def search(base, product, divisor, offset):
    i = 0
    found = False
    while not found:
        test = base + i * product
        if (test + offset) % divisor == 0:
            found = True
            return test

        i += 1

tested = []
current_sol = 0
for i, bus in enumerate(busses):

    if i != 0:
        current_sol = search(current_sol, np.product(tested), bus['id'], bus['offset'])

    tested.append(bus['id'])

print("part 2: " + str(current_sol))