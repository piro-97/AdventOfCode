import utils
import numpy as np
import re
from copy import deepcopy

DAY = 5

def parse_stack(string :str) -> "int, list":
    l = []
    n = -1
    for s in string:
        if s.isalpha():
            l.append(s)
        if s.isnumeric():
            n = int(s)

    return n, l


# parse input and create stacks
lines = utils.read_input(DAY)
split_idx = lines.index("")
stack_lines = utils.to_np_array(lines[:split_idx], dtype=str)
stack_lines = np.flip(np.transpose(stack_lines))

stacks = {}
for line in stack_lines:
    index, stack = parse_stack(line)
    if index > 0:
        stacks[index] = stack

stacks2 = deepcopy(stacks)

# part 1

pattern = re.compile(r"^move (?P<quantity>\d*?) from (?P<source>\d*?) to (?P<destination>\d*?)$")

for line in lines[split_idx + 1:]:
    match = pattern.match(line)
    quantity, source, destination = map(int, match.group("quantity", "source", "destination"))

    q = quantity
    while q > 0:
        stacks[destination].append(stacks[source].pop())
        q -= 1

    stacks2[destination] += stacks2[source][-quantity:]
    del stacks2[source][-quantity:]

utils.print_answer(1, "".join(map(lambda x: x[1].pop() , sorted(stacks.items()))))
utils.print_answer(2, "".join(map(lambda x: x[1].pop() , sorted(stacks2.items()))))
